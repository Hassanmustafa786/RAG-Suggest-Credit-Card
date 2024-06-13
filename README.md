# Credit Card Suggestor Chatbot

This project is a chatbot that suggests credit cards based on user queries. It scrapes content from a specified website, converts the content into embeddings, and uses Retrieval-Augmented Generation (RAG) to answer questions accordingly. The project is built using Flask.

## Features

- Scrapes credit card comparison data from a website.
- Converts website content into embeddings.
- Utilizes RAG to provide credit card suggestions based on user queries.
- Built using Flask framework.

## Project Structure

- `app.py` - The main Flask application code.
- `templates/` - Contains HTML templates for the web interface.
- `static/` - Contains static files (CSS, JS, images) if needed.
- `requirements.txt` - Lists all the required libraries for the project.
- `README.md` - Project documentation.

## Libraries Used

- `flask`
- `llama_index`
- `dotenv`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Hassanmustafa786/Detection-System.git
    cd RAG Suggest Credit Card
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables by creating a `.env` file in the root directory:

    ```ini
    OPENAI_API_KEY=your_openai_api_key
    ```

## Running the Application

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

1. Navigate to the home page of the application.
2. Enter your query about credit card suggestions.
3. The chatbot will scrape the content from the specified website, convert it into embeddings, and provide a suggestion based on your query.

## Example Projects

Here are some example projects demonstrating my proficiency in Python and Data Science:

- [Detection System](https://github.com/Hassanmustafa786/RAG-Suggest-Credit-Card/)

## Contact

If you have any questions or would like to discuss further, feel free to reach out to me at [your email].

---

**Hafiz Hassan Mustafa**  
[LinkedIn](https://www.linkedin.com/in/hafiz-hassan-mustafa-692b391b4/)
