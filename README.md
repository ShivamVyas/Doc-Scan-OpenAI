# DocScanner - Personalized Chatbot

Welcome to DocScanner, a personalized chatbot program designed to help you with document scanning and answering questions related to the documents you upload. This readme file will guide you through the process of cloning the repository and installing the required dependencies to get started.

## Installation

To use DocScanner, please follow the steps below:

1. Clone the repository to your local machine using the following command:

   ```bash
   git clone repository_url](https://github.com/ShivamVyas/Doc-Scan-OpenAI.git
   ```
2. Update 'env' file with your OpenAI Key
   
3. Add OpenAI to your machine enviroment variable
   Step 1: Open CMD prompt
   Step 2: Run the following in the cmd prompt, replacing <yourkey> with your API key:
   ```bash
   setx OPENAI_API_KEY “<yourkey>”
   ```
   Step 3: To validate the OpenAI Key on your machine, use the cmd command:
   ```bash
   echo %OPENAI_API_KEY%
   ```
4. Install the required dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

   This command will install all the necessary Python packages specified in the `requirements.txt` file.

5. After the installation is complete, you are ready to start using DocScanner!

## Usage

To use DocScanner, follow the steps below:

1. Make sure you have the required documents you want to scan and ask questions about. Ensure that the documents are in a compatible format (e.g., PDF, image files, etc.).

2. Run the DocScanner program using the following command:

   ```bash
   streamlit run app.py
   ```

3. This command will start the DocScanner application. A browser window will open with the chat interface.

4. The program will prompt you to upload the document files you want to scan. Provide the paths to the document files when prompted. You can upload multiple files by providing their paths one by one.

5. Once the documents are uploaded, the chatbot will be ready to answer your questions about the documents. You can ask questions by typing them into the chat interface.

6. The chatbot will analyze the documents and provide relevant answers based on the content it has processed. You can continue asking questions or request additional documents to be scanned.

7. To exit the program, simply close the browser window or terminate the program by pressing Ctrl+C in the command line where the program is running.

## Contact

If you have any questions, issues, or suggestions regarding DocScanner, please contact at https://www.linkedin.com/in/shivamvyas.

Thank you for using DocScanner! We hope it proves to be a helpful tool for your document scanning and question-answering needs.

## License

The Document Scanner with OpenAI ChatGPT project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code in accordance with the terms specified in the license.

## Disclaimer

The Document Scanner with OpenAI ChatGPT project is an independent project and not officially affiliated with OpenAI. It utilizes the OpenAI API to access the ChatGPT model for document analysis and information extraction.
