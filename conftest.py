import pytest
from fastapi.testclient import TestClient
from notes_app import app, NotesApp

@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)

@pytest.fixture
def notes_app():
    """Create a fresh NotesApp instance for each test"""
    return NotesApp()

@pytest.fixture
def sample_note():
    """Return sample note data"""
    return {"content": "Test note content"}

@pytest.fixture(autouse=True)
def reset_notes_app():
    """Reset the notes app state before each test"""
    app.dependency_overrides = {}
    yield
    # Clear all notes after each test
    app.notes_app = NotesApp()

@pytest.fixture
def note_in_db(client, sample_note):
    """Create a note and return its response data"""
    response = client.post("/notes/", json=sample_note)
    return response.json()

@pytest.fixture
def multiple_notes(client):
    """Create multiple notes and return their response data"""
    notes = [
        {"content": f"Test note {i}"} 
        for i in range(3)
    ]
    responses = []
    for note in notes:
        response = client.post("/notes/", json=note)
        responses.append(response.json())
    return responses
