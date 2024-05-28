
import requests

def test_create_faiss_database(base_url):
    response = requests.post("http://localhost:5008/CreateFAISSDatabase", json={"base_url": base_url})
    assert response.status_code == 200
    print("FAISS Database Creation: ", response.json())

def test_chat(base_url, message):
    response = requests.post("http://localhost:5008/Chat", json={"base_url": base_url, "message": message})
    assert response.status_code == 200
    print("Chat Response: ", response.json())

if __name__ == "__main__":
    base_url = "http://localhost/wordpress"
    test_create_faiss_database(base_url)
    test_chat(base_url, "show me all comments with date")
