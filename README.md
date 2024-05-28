# Wasserstoff AI Fullstack Developer Task

## Description

This project is a Flask-based web application designed to create and manage a FAISS vector database from WordPress site content and perform retrieval-augmented generation (RAG) for question answering (QA) tasks. The application extracts content from a WordPress site, preprocesses it, and uses FAISS for vector storage and retrieval, combined with a large language model (LLM) for generating answers to user queries..

## Features
  **FAISS Vector Database Creation**: Automatically creates and updates a FAISS vector database from a specified WordPress site's content.
  
  **Content Preprocessing**: Extracts and preprocesses text content from WordPress posts, pages, and comments.
  
  **Question Answering**: Uses RAG to provide answers to user queries based on the content stored in the FAISS database.
  
  **Flask Web Interface**: Provides a simple web interface for interacting with the system.

### This is the interface ![Screenshot from 2024-05-28 11-22-52](https://github.com/SidRaza786/wasserstoff/assets/107919240/5c1998a5-f5e1-47f1-bf52-792d5c579aac)
    
## Installation
### Prerequisites
    Python 3.8+
    Flask
    requests
    BeautifulSoup4
    langchain
    Hugging Face Transformers
    FAISS
    Google Generative AI (for the LLM)
    


## Setup

1. Clone the repository and create a virtual-environment and activate.
    ```sh
    https://github.com/SidRaza786/wasserstoff.git
    cd AiTask
    
    python3 -m venv chat
    source chat/bin/activate
    ```
    

 2. Install the required packages.
    ```sh
    pip install -r requirements.txt
    ```

 3. Set up environment variables.Create a **.env** file in the project root directory and add your Hugging Face and Google API keys.

    
   ```sh
    HUGGINGFACE_TOKEN=your_huggingface_token
    GOOGLE_API_KEY=your_google_api_key
   ```

  
4. tart the Flask server.
    ```sh
    python3 app.py
    ```
    The server will run on http://0.0.0.0:5008

### API Endpoints
## 1.Create FAISS Database
 
  **URL**: /CreateFAISSDatabase
   
  **Method**: POST
   
  **Request Body**:
  
   
    {
    "base_url": https://www.example.com
    }

**Response** Success: FAISS Vector Database has been created.

## 2. Chat

  **URL:** /Chat
  
  **Method:** POST
  
  **Request Body**:

     {
       "base_url": http://localhost/wordpress,
       "message": "user query"
      }

**Response:**


     {
     "response": "Response: your_answer",
     "response_time": response_time_in_seconds
     }



## Acknowledgments
    Flask
    
    FAISS
    
    Hugging Face
    
    Google Generative AI


 
