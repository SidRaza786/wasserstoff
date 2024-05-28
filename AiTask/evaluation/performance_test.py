# performance_test.py
import requests
import time

def test_response_time(base_url, message):
    start_time = time.time()
    response = requests.post("http://localhost:5008/Chat", json={"base_url": base_url, "message": message})
    end_time = time.time()
    response_time = end_time - start_time
    print("Response Time: ", response_time)
    print("Response: ", response.json())

if __name__ == "__main__":
    base_url = "http://localhost/wordpress"
    test_response_time(base_url, "All posts name")
