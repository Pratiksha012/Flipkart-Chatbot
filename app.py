from flask import Flask, render_template, request
from flipkart_scraper import scrape_flipkart_products
import webbrowser
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

app = Flask(__name__)

def get_product_info(search_query, num_pages):
    try:
        products = scrape_flipkart_products(search_query, num_pages)
        if not products:
            return [], "No products found. Please try again with different search terms."
        return products, None
    except Exception as e:
        # Log the error or handle it appropriately
        error_message = f"Error occurred: {str(e)}"
        return [], error_message

def format_product_info(products):
    if not products:
        return "Sorry, I couldn't find any products matching your query."

    response = "Here are some products I found:<br><br>"
    for index, product in enumerate(products, start=1):
        response += f"Product {index}:<br>"
        # Add image tag
        response += f"<img src='{product['Image']}' class='product-image' alt='Product Image'><br>"
        response += f"Name: <a href='{product['Link']}' target='_blank'>{product['Name']}</a><br>"
        response += f"Price: {product['Price']}<br>"
        response += f"Ratings: {product.get('Ratings', 'Not available')}<br><br>"
    return response

def detect_greeting(user_input):
    greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening","hola","sup","whatsup","wassup","bonjour"]
    gratitude_expressions = ["thank you", "thanks", "appreciate it","thank you so much"]
    
    # Check if the user input contains any greetings
    for greeting in greetings:
        if greeting in user_input.lower():
            return f"{greeting.capitalize()}! How can I help you today?"
    
    # Check if the user input contains expressions of gratitude
    for gratitude in gratitude_expressions:
        if gratitude in user_input.lower():
            return "You're welcome! Feel free to ask if you need any assistance."
    
    return None

@app.route("/")
def index():
    default_message = "Hello! I'm your friendly Flipkart Chatbot. How can I assist you today?"
    return render_template("chat.html", default_message=default_message)

@app.route("/get_products", methods=["POST"])
def get_products():
    user_query = request.form["user_query"].strip()
    num_pages = request.form.get("num_pages", type=int, default=1)

    # Check if the user greeted or expressed gratitude
    response = detect_greeting(user_query)
    if response:
        return f"{response}"
    if not user_query:
        return "Please enter a valid search query."

    if num_pages <= 0:
        return "Number of pages must be a positive integer."

    # Tokenize user query
    tokens = word_tokenize(user_query)

    # Remove stopwords
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

    # Join filtered tokens back into a string for search query
    search_query = ' '.join(filtered_tokens)

    products, error_message = get_product_info(search_query, num_pages)
    if error_message:
        return error_message

    product_info = format_product_info(products)

    return product_info

def open_browser():
    # Check if the script is being run directly
    if __name__ == "__main__":
        webbrowser.open("http://127.0.0.1:8080/")

if __name__ == "__main__":
    open_browser()
    app.run(host='0.0.0.0', port=8080, debug=True)
