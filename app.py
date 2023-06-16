# UI Library
import streamlit as st

# Time and Random library for operation progress bar
import time
import random

# URL Image Extractions
import urllib.request
from PIL import Image

# Doc Readers
import docx2txt
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

# Environment Variable 
from dotenv import load_dotenv

# Open AI And Facebook's Similarity Search Libraries
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.callbacks import get_openai_callback
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain 

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# Adding Background Image and Removing Watermark
def html_configurations():
    st.markdown(
          f"""
          <style>
          .stApp {{
              background-image: url("https://images.unsplash.com/photo-1518655048521-f130df041f66?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2670&q=80");
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
    file_list = st.file_uploader(":orange[**Please upload your PDF or DOCX files here:**]", type=["pdf","docx"], accept_multiple_files=True) 
    
    # Extract the text from each PDF
    if file_list:
      text = ""
      for file in file_list:
        text += file.name
        if ".pdf" in file.name:
          pdf_reader = PdfReader(file)
          for page in pdf_reader.pages:
            text += page.extract_text()
        elif ".docx" in file.name:
           text += docx2txt.process(file)

      # Split text into chunks
      text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
      chunks = text_splitter.split_text(text)
      
      # Takes environment variables from env file
      load_dotenv()

      # Creating OpenAI embeddings and using it with Facebook AI Similarity Search
      embeddings = OpenAIEmbeddings()
      faiss = FAISS.from_texts(chunks, embeddings)
      
      #Initializing varibles in the first instance to save in memory and prevent reset
      if "chat_history" not in st.session_state:
        st.balloons()
        memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
        llm = ChatOpenAI()
        conversation_chain = ConversationalRetrievalChain.from_llm(
          llm=llm,
          retriever=faiss.as_retriever(),
          memory=memory
        )
        st.session_state.conversation = conversation_chain
        st.session_state.chat_history = memory
        st.session_state.openai_cost = [] 
      
      user_question = st.text_input(":orange[**How can I help you?**]", placeholder="Enter your question here")  
      
      #Use the code below for real time progress status
      #with st.spinner(text="Operation in Progress"):
      #   if user_question...

      if user_question:
        # Progress bar not configured with threading (Just for show)
        progress_bar = st.progress(0);
        r=random.randint(30,60)
        for a in range(r):
          time.sleep(0.1)
          progress_bar.progress(a+1,text="**Operation in progress ⏳**")
        
        # Token Cost
        with get_openai_callback() as cost:
          response = st.session_state.conversation({'question': user_question})
        st.session_state.openai_cost.append(cost.total_cost)

        for index, message in enumerate(response['chat_history']):
          if index%2==0:
            st.write("<h6 style='color:#d95a00;'>"+message.content+"</h6>", unsafe_allow_html = True)
            st.write("**Cost of Operation: :green[$"+str('%.6f'%(st.session_state.openai_cost[int(index/2)]))+"]**")
          else: 
            st.write("<h6>"+message.content+"</h6>", unsafe_allow_html = True)

        #Progress bar not configured with threading (Just for show)
        for i in range(r,100):
          time.sleep(0.01)
          progress_bar.progress(i+1,text="**Operation in progress ⏳**")
        progress_bar.progress(100, text="**Operation Success ✅**")
        
       

      

        

        
        
    

if __name__ == '__main__':
    main()