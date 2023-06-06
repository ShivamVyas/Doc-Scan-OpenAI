import streamlit as st
import docx2txt
import time
import random
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


# Adding Background Image and Removing Watermark
def html_configurations():
    st.markdown(
          f"""
          <style>
          .stApp {{
              background-image: url("https://i.imgur.com/5io8Mnn.jpeg");
              background-attachment: fixed;
              background-size: cover;
          }}
         </style>
         """,
         unsafe_allow_html=True
      )
    hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

def main():
    # URL Title and Logo
    urllib.request.urlretrieve('https://ontariotechu.ca/favicon.ico', "img.png")
    img = Image.open("img.png")
    st.set_page_config(page_title="DocScanner", page_icon=img)
    
    # Adding Background Image and Removing Watermark
    html_configurations() 

    # Title
    st.markdown("<h2>\nDocument Scanner - Personalized ChatBot 📖</h2>", unsafe_allow_html = True)
    
    #Change Text Color
    #st.markdown("This text is <span style='color:#ff6600'>colored pink</span>", unsafe_allow_html=True)
    
    # Upload File Prompt
    file_list = st.file_uploader("**Please upload your PDF or DOCX files here:**", type=["pdf","docx"], accept_multiple_files=True) 
    
    # Extract the text from each PDF
    if file_list:
      text = ""
      for file in file_list:
        if ".pdf" in file.name:
          pdf_reader = PdfReader(file)
          for page in pdf_reader.pages:
            text += page.extract_text()
        elif ".docx" in file.name:
           text += docx2txt.process(file)

      # Split text into chunks
      text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
      chunks = text_splitter.split_text(text)
      
      load_dotenv()
      # Using Facebook's library creating embeddings
      embeddings = OpenAIEmbeddings()
      knowledge_base = FAISS.from_texts(chunks, embeddings)
      
      # Run OPENAI and Show User Input
      user_question = st.text_input(":orange[**How can I help you?**]")
      if user_question:
        docs = knowledge_base.similarity_search(user_question)
        
        llm = OpenAI()
        chain = load_qa_chain(llm, chain_type="stuff")
        
        
        # Progress bar not configured with threading (Just for show)
        progress_bar = st.progress(0);
        r=random.randint(30,60)
        for a in range(r):
          time.sleep(0.1)
          progress_bar.progress(a+1,text=":orange[**Operation in progress ⏳**]")
        
        # Gather Response with Token Cost
        with get_openai_callback() as cb:
          response = chain.run(input_documents=docs, question=user_question)

        # Progress bar not configured with threading (Just for show)
        for i in range(r,100):
          time.sleep(0.01)
          progress_bar.progress(i+1,text=":orange[**Operation in progress ⏳**]")
        progress_bar.progress(100, text=":orange[**Operation Success ✅**]")

        # Token Cost
        st.write(cb)
        # AIResponse
        st.write(response)
        
    

if __name__ == '__main__':
    main()