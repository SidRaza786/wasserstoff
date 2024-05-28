# chain_of_thought_test.py
import requests

def test_chain_of_thought(base_url, message):
    response = requests.post("http://localhost:5008/Chat", json={"base_url": base_url, "message": message})
    data = response.json()
    print("Response: ", data["response"])
    print("Chain of Thought Coherence: To be manually evaluated from the response.")

if __name__ == "__main__":
    base_url = "http://localhost/wordpress"
    test_chain_of_thought(base_url, "Tell me all english teacher's name")
