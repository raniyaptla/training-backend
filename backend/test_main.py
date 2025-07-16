import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
import sys
import os

# Add the current directory to Python path so we can import main
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Mock the asyncpg module since we don't need it for basic tests
sys.modules['asyncpg'] = __import__('unittest.mock').mock.MagicMock()

from main import app

# Create a test client
client = TestClient(app)

def test_app_creation():
    """Test if the FastAPI app can be created"""
    assert app is not None
    assert app.title == "Simple PostgreSQL Backend"
    print("✅ App creation test passed!")

def test_home_endpoint_structure():
    """Test the home endpoint without database"""
    # Mock the database connection to be None (simulating no connection)
    with patch('main.db_connection', None):
        response = client.get("/")
        
        # Check if the response is successful
        assert response.status_code == 200
        
        # Check if the response is JSON
        data = response.json()
        assert "message" in data
        
        # Should say database is not connected when db_connection is None
        assert "not connected" in data["message"]
        
        print("✅ Home endpoint test passed!")

def test_home_endpoint_with_mock_db():
    """Test the home endpoint with mocked database"""
    # Mock the database connection to exist
    with patch('main.db_connection', 'mock_connection'):
        response = client.get("/")
        
        # Check if the response is successful
        assert response.status_code == 200
        
        # Check if the response is JSON
        data = response.json()
        assert "message" in data
        
        # Should say database is connected when db_connection exists
        assert "connected" in data["message"]
        
        print("✅ Home endpoint with database test passed!")

def test_api_docs_available():
    """Test if API documentation is available"""
    response = client.get("/docs")
    assert response.status_code == 200
    print("✅ API docs test passed!")

# Run this if you want to test manually
if __name__ == "__main__":
    test_app_creation()
    test_home_endpoint_structure()
    test_home_endpoint_with_mock_db()
    test_api_docs_available()
    print("🎉 All tests passed!")