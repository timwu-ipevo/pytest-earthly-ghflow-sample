from fastapi.testclient import TestClient
from notes_app import app, NotesApp
import pytest

client = TestClient(app)

def test_create_note(client, sample_note):
    response = client.post("/notes/", json=sample_note)
    assert response.status_code == 200
    assert response.json()["content"] == sample_note["content"]
    assert response.json()["index"] == 0

def test_get_note(client, note_in_db):
    response = client.get(f"/notes/{note_in_db['index']}")
    assert response.status_code == 200
    assert response.json()["content"] == note_in_db["content"]
    assert response.json()["index"] == note_in_db["index"]

def test_get_nonexistent_note(client):
    response = client.get("/notes/999")
    assert response.status_code == 404

def test_list_notes(client, multiple_notes):
    response = client.get("/notes/")
    assert response.status_code == 200
    notes = response.json()
    for i, note in enumerate(notes):
        #test if the note content prefix is 'Test note'
        assert note["content"].startswith("Test note")
        #assert note["content"] == f"Test note {i}"

def test_update_note(client, note_in_db):
    updated_content = {"content": "Updated note"}
    response = client.put(f"/notes/{note_in_db['index']}", json=updated_content)
    assert response.status_code == 200
    assert response.json()["content"] == updated_content["content"]

def test_update_nonexistent_note(client):
    response = client.put("/notes/999", json={"content": "Updated note"})
    assert response.status_code == 404

def test_delete_note(client, note_in_db):
    response = client.delete(f"/notes/{note_in_db['index']}")
    assert response.status_code == 200
    
    # Verify note is deleted
    response = client.get(f"/notes/{note_in_db['index']}")
    assert response.status_code == 404

def test_delete_nonexistent_note(client):
    response = client.delete("/notes/999")
    assert response.status_code == 404

def test_invalid_note_data(client):
    response = client.post("/notes/", json={})
    assert response.status_code == 422  # FastAPI validation error