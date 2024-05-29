import pytest
from app import app

#from task import create_task, get_all_tasks,update_task, delete_task


@pytest.fixture
def client():
    app.config['TESTING']=True
    with app.test_client() as client:
        yield client
        
def test_login(client):
    response = client.get('/login')
    assert response.status_code == 200
    
        
def test_register(client):
    response = client.get('/register')
    assert response.status_code == 200
    
  
def test_create_task(client):
   response = client.get('/estimationform')
   assert response.status_code == 200
    
def test_update_task(client):
    response = client.get('/update/66517d5118d2208990cc680d')
    assert response.status_code == 200
    
def test_delete(client):
    response = client.get('/delete/66517d5118d2208990cc680d')

    assert response.status_code == 200 # Redirect with status code 302 (FOUND)

    assert response.status_code == 302 # Redirect with status code 302 (FOUND)

def test_estimate(client):
    response = client.get('/estCalculate')
    assert response.status_code == 200 # Redirect with status code 302 (FOUND)

def test_logout(client):
    response = client.get('/logout')
    assert response.status_code == 302 # Redirect with status code 302 (FOUND)



