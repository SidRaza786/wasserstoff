# app.py
from flask import Flask, request, jsonify
import time
from data_preprocessing_unit import DataProcessor
from retrieval_generation import RAGSystemWithCOT
from data_ingestion import FaissVDB
import os

app = Flask(__name__)

process_data = DataProcessor()
WordpressRAG = RAGSystemWithCOT()
Faiss_VDB = FaissVDB()

@app.route("/CreateFAISSDatabase", methods=["POST"])
def create_faiss_database():
    if request.method == 'POST':
        data = request.json
        base_url = data["base_url"]
        faiss_database_status = Faiss_VDB.CreateFaissVDB(base_url, "done")
        if faiss_database_status:
            return jsonify(message=f'FAISS Vector Database has been created for {base_url}')
    

@app.route("/Chat", methods=["GET", "POST"])
def chat():
    if request.method in ['POST', 'GET']:
        data = request.json
        base_url = data["base_url"]
        user_query = data["message"]
        retriever = Faiss_VDB.Create_and_Update_FaissVDB(base_url, "done")
        rag_chain = WordpressRAG.RAGResponseWithCOT(retriever)
        
        start_time = time.time()
        response = rag_chain.invoke(user_query)
        end_time = time.time()
        
        response_time = end_time - start_time
        return jsonify(response=f"Response: {response}", response_time=response_time)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5008, debug=True)
