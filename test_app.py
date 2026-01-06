from app import app

def test_home():
    # Create a test client
    client = app.test_client()
    
    # Simulate a GET request to the home page
    response = client.get("/")
    
    # Check that the status code is 200
    assert response.status_code == 200
    
    # Check that the main heading is in the HTML
    assert b"Welcome to My Flask App!" in response.data
    
    # check that the paragraph exists
    assert b"This is a simple HTML page served by Flask." in response.data
