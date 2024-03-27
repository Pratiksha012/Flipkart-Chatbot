# Flipkart Chatbot (Prototype)

## Description
The Flipkart Chatbot is a prototype application designed to assist users in searching for products on the Flipkart website. It utilizes web scraping techniques to gather product information and presents it in a chat interface.

## Features
- **Chat Interface:** Users can interact with the chatbot using a simple text input field.
- **Product Search:** Users can enter their search queries, and the chatbot fetches relevant product information from Flipkart.
- **Greeting and Gratitude Detection:** The chatbot can detect greetings and expressions of gratitude from users and respond accordingly.
- **Error Handling:** The application includes error handling mechanisms to address issues such as invalid user input or failed web scraping attempts.

## Technologies Used
- **Python:** The backend logic of the application is written in Python.
- **Flask:** Flask is used as the web framework to create the server and handle HTTP requests.
- **Beautiful Soup:** Beautiful Soup is utilized for web scraping Flipkart's product data.
- **HTML/CSS/JavaScript:** Frontend components of the chat interface are built using HTML, CSS, and JavaScript.
- **NLTK:** NLTK (Natural Language Toolkit) is used for text processing, including stop word removal and greeting detection.

## Installation and Usage
1. Clone the repository to your local machine.
2. Web Scrape flipkart website using `flipkart_scraper.py` file.
3. Run the Flask application by executing the `app.py` file.
4. Access the application through your web browser at `http://localhost:8080`.
5. 
6. Enter your queries in the chat input field and click submit to receive product recommendations.

## Future Improvements
1. **Enhanced User Interface:** Improve the aesthetics and functionality of the chat interface.
2. **Advanced Search Filters:** Allow users to apply filters such as price range, brand, or category.
3. **User Authentication:** Implement user authentication to provide personalized recommendations.
4. **Natural Language Understanding (NLU):** Integrate NLU techniques to improve the chatbot's understanding of user queries.
5. **Performance Optimization:** Optimize web scraping algorithms for better performance and reliability.

## Contributing
Contributions to the project are welcome. If you have any suggestions, bug fixes, or feature enhancements, feel free to open an issue or submit a pull request on GitHub.

## Acknowledgments
- Thanks to Flipkart for providing access to their product data.
- Special thanks to the open-source community for the tools and libraries used in this project.
