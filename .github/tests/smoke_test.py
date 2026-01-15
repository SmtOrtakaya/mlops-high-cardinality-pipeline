import requests
def test_service_is_up():
    response = requests.get("http://localhost:5000/health")
    assert response.status_code == 200
if __name__ == "__main__": test_service_is_up()
