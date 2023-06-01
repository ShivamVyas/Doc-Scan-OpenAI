# Document Scanner with OpenAI ChatGPT

The Document Scanner with OpenAI ChatGPT is a project that utilizes OpenAI's ChatGPT API to analyze and extract details from various types of documents. It provides a convenient way to scan documents and obtain information using natural language queries.

## Features

- **Document Scanning:** The project allows you to scan different types of documents, such as PDFs, images, and text files.
- **Information Extraction:** By using the OpenAI ChatGPT API, the project can extract relevant details from the scanned documents based on natural language queries.
- **User-friendly Interface:** The project provides an intuitive interface for interacting with the scanner, making it easy for users to input documents and obtain information.

## Setup Instructions

Follow the steps below to set up and run the Document Scanner with OpenAI ChatGPT project:

1. **Clone the Repository:** Begin by cloning the project repository to your local machine using the following command:
    ```
    git clone https://github.com/your-username/document-scanner.git
    ```

2. **Install Dependencies:** Navigate to the project directory and install the required dependencies by running the following command:
    ```
    cd document-scanner
    pip install -r requirements.txt
    ```

3. **OpenAI API Configuration:** To access the OpenAI ChatGPT API, you will need an API key. If you don't have one, sign up for an account at [OpenAI](https://openai.com/) and obtain your API key.

    - Create a new file named `.env` in the project directory.
    - Open the `.env` file and add the following line, replacing `<YOUR_API_KEY>` with your actual API key:
        ```
        OPENAI_API_KEY=<YOUR_API_KEY>
        ```

4. **Start the Application:** Once the setup is complete, you can run the application using the following command:
    ```
    python app.py
    ```

    The application will start, and you will see instructions and prompts in the terminal.

## Usage

1. When the application starts, it will prompt you to provide the path to the document you want to scan. Enter the path or filename and press Enter.

2. The document will be scanned, and the application will display a confirmation message along with some basic details about the document, such as the file type, size, and number of pages.

3. Next, you can enter a natural language query to obtain specific information from the document. For example, you can ask questions like:
    - "What is the title of the document?"
    - "Who is the author of the document?"
    - "How many pages does the document have?"

    The application will send your query to the OpenAI ChatGPT API and display the extracted information.

4. You can continue to enter queries or provide a new document path to scan additional documents.

## Contributing

Contributions to the Document Scanner with OpenAI ChatGPT project are welcome! If you encounter any issues, have suggestions for improvements, or would like to add new features, please submit a pull request on the project's GitHub repository.

When contributing, please ensure that you follow the existing coding style and conventions, write appropriate tests, and provide clear documentation.

## License

The Document Scanner with OpenAI ChatGPT project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code in accordance with the terms specified in the license.

## Disclaimer

The Document Scanner with OpenAI ChatGPT project is an independent project and not officially affiliated with OpenAI. It utilizes the OpenAI API to access the ChatGPT model for document analysis and information extraction.
