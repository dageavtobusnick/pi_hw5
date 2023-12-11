from fastapi.testclient import TestClient 
from main import app


client = TestClient(app) 
def test_read_main_1(): 
    response = client.get("/") 
    assert response.status_code == 200 
    assert response.json() == {"message": "This is root page"}
    
def test_read_main_2(): 
    response = client.post("/en_ru/", json={"text": "I like machine learning!"})
    assert response.status_code == 200 
    print(response.json())
    assert response.json() == {"translated_text": "Я люблю машинное обучение!"}
    
def test_read_main_3(): 
    response = client.post("/en_ru/", json=None) 
    assert response.status_code == 422
    
def test_read_main_4(): 
    response = client.post("/en_ru/", json={"text": None}) 
    assert response.status_code == 422
    
def test_read_main_5(): 
    response = client.post("/en_ru/", json={"text": ""}) 
    assert response.status_code == 400 
    