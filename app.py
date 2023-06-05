import streamlit as st
import time
import urllib.request
from PIL import Image
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

def main():
    #URL Title and Logo
    urllib.request.urlretrieve('https://ontariotechu.ca/favicon.ico', "img.png")
    img = Image.open("img.png")
    st.set_page_config(page_title="DocScanner", page_icon=img)
    
    #Hiding Steamlit Logo and Settings
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    
    #Title
    st.header("Document Scanner - Personalized ChatBot 📖")
    
    # # upload file
    # pdf_list = st.file_uploader("Please upload your PDF files", type="pdf", accept_multiple_files=True) 
    
    # # extract the text
    # if pdf_list:
    #   for pdf in pdf_list:
    #     pdf_reader = PdfReader(pdf)
    #     text = ""
    #     for page in pdf_reader.pages:
    #       text += page.extract_text()
    
    # upload file
    pdf = st.file_uploader("Please upload your PDF files", type="pdf") 
    # extract the text
    if pdf:
      pdf_reader = PdfReader(pdf)
      text = ""
      for page in pdf_reader.pages:
        text += page.extract_text()  

      # split into chunks
      text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
      )
      chunks = text_splitter.split_text(text)
      
      load_dotenv()
      # create embeddings
      embeddings = OpenAIEmbeddings()
      knowledge_base = FAISS.from_texts(chunks, embeddings)
      
      #show user input 
      user_question = st.text_input("How can I help you?")
      if user_question:
        docs = knowledge_base.similarity_search(user_question)
        
        llm = OpenAI()
        chain = load_qa_chain(llm, chain_type="stuff")
        progress_bar = st.progress(0);
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=user_question)
        
        #Progress bar not configured with threading (Just for show)
        for process_completed in range(100):
          time.sleep(0.01)
          progress_bar.progress(process_completed+1)
        st.write(cb)
        st.write(response)
        
    

if __name__ == '__main__':
    main()