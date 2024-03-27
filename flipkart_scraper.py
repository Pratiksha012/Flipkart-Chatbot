from bs4 import BeautifulSoup
import requests

def scrape_flipkart_products(search_query, num_pages):
    base_url = 'https://www.flipkart.com'
    search_url = f'{base_url}/search?q={search_query.replace(" ", "+")}'
    all_products = []
    for page in range(1, num_pages + 1):
        page_url = f'{search_url}&page={page}'
        response = requests.get(page_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # First set of products
            products_set1 = soup.find_all('div', {'class': '_1AtVbE col-12-12'})
            for product in products_set1:
                try:
                    product_name_tag = product.find('a', {'class': 'IRpwTa'})
                    product_price_tag = product.find('div', {'class': '_30jeq3'})
                    if product_name_tag and product_price_tag:
                        product_name = product_name_tag.text.strip()
                        product_price = product_price_tag.text.strip()
                        product_link = base_url + product_name_tag['href']
                        product_ratings_tag = product.find('span', {'class': '_2_R_DZ'})
                        product_ratings = product_ratings_tag.text.strip() if product_ratings_tag else "Ratings not available"
                        product_image_tag = product.find('img', {'class': '_2r_T1I'})
                        product_image = product_image_tag['src'] if product_image_tag else "Image not available"
                        all_products.append({'Name': product_name, 'Price': product_price, 'Link': product_link, 'Ratings': product_ratings, 'Image': product_image})
                except AttributeError:
                    print("Skipping product due to missing data")
                    
            # Second set of products
            products_set2 = soup.find_all('div', {'class': '_1AtVbE'}) or soup.find_all('div', {'class': '_4ddWXP'})
            for product in products_set2:
                try:
                    product_name_tag = product.find('div', {'class': '_4rR01T'}) or product.find('a', {'class': 's1Q9rs'})
                    product_price_tag = product.find('div', {'class': '_30jeq3'})
                    product_link_tag = product.find('a', {'class': '_1fQZEK'}) or product.find('a', {'class': 's1Q9rs'})
                    product_ratings_tag = product.find('div', {'class': '_3LWZlK'})
                    product_image_tag = product.find('img', {'class': '_396cs4'})
                    if all((product_name_tag, product_price_tag, product_link_tag, product_ratings_tag, product_image_tag)):
                        product_name = product_name_tag.text.strip()
                        product_price = product_price_tag.text.strip()
                        product_link = base_url + product_link_tag['href']
                        product_ratings = product_ratings_tag.text.strip()
                        product_image = product_image_tag['src']
                        all_products.append({'Name': product_name, 'Price': product_price, 'Link': product_link, 'Ratings': product_ratings, 'Image': product_image})
                except AttributeError:
                    print("Skipping product due to missing data")
        else:
            print(f"Failed to retrieve page {page_url}: {response.status_code}")
    return all_products
