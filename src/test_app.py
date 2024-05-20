import pytest
from fastapi.testclient import TestClient
from app import app
client = TestClient(app)

# Test the /recommendations endpoint
def test_recommendations_success():
    response = client.get("/recommendations", params={"user_id": 1, "returnMetadata": False})
    assert response.status_code == 200
    data = response.json()
    
    items = data.get("items")[0]    
    for data_dict in items:
        for data_dict_key in data_dict:
            assert  len(data_dict_key) == len("id")

    assert "items" in data
    assert isinstance(data["items"], list)

def test_recommendations_user_not_found():
    response = client.get("/recommendations", params={"user_id": -1, "returnMetadata": False})
    assert response.status_code == 200
    data = response.json()
    assert data == {"status": "fail, not have user_id"}

    

def test_recommendations_with_metadata():
    response = client.get("/recommendations", params={"user_id": 1, "returnMetadata": True})
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert isinstance(data["items"], list)
    if len(data["items"]) > 0:
        assert "title" in data["items"][0][0]
        assert "genres" in data["items"][0][0]

# Test the /features endpoint
def test_features_success():
    response = client.get("/features", params={"user_id": 1})
    assert response.status_code == 200
    data = response.json()
    assert "features" in data
    assert "histories" in data["features"]
    assert isinstance(data["features"]["histories"], list)

def test_features_user_not_found():
    response = client.get("/features", params={"user_id": -1})
    assert response.status_code == 200
    data = response.json()
    assert "features" in data
    assert data["features"]["histories"] == []


if __name__ == "__main__":
   pytest.main()    