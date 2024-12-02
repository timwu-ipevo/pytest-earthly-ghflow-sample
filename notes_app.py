from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

class Note:
    def __init__(self, content: str):
        self.content = content

class NoteRequest(BaseModel):
    content: str

class NoteResponse(BaseModel):
    content: str
    index: int

class NotesApp:
    def __init__(self):
        self.notes_list = []

    def add_note(self, content):
        new_note = Note(content)
        self.notes_list.append(new_note)
        return "Note added successfully"
    def del_note(self, index):
        try:
            del self.notes_list[index]
            return "Note deleted successfully"
        except IndexError:
            return "Index out of range"

    def get_note(self, index):
        try:
            return self.notes_list[index].content
        except IndexError:
            return "Index out of range"

    def edit_note(self, index, content):
        try:
            self.notes_list[index].content = content
            return "Note edited successfully"
        except IndexError:
            return "Index out of range"

app = FastAPI()
notes_app = NotesApp()

@app.post("/notes/", response_model=NoteResponse)
def create_note(note: NoteRequest):
    notes_app.add_note(note.content)
    return NoteResponse(
        content=note.content,
        index=len(notes_app.notes_list) - 1
    )

@app.get("/notes/{index}", response_model=NoteResponse)
def read_note(index: int):
    content = notes_app.get_note(index)
    if content == "Index out of range":
        raise HTTPException(status_code=404, detail="Note not found")
    return NoteResponse(content=content, index=index)

@app.get("/notes/", response_model=List[NoteResponse])
def list_notes():
    return [
        NoteResponse(content=note.content, index=i)
        for i, note in enumerate(notes_app.notes_list)
    ]

@app.put("/notes/{index}", response_model=NoteResponse)
def update_note(index: int, note: NoteRequest):
    result = notes_app.edit_note(index, note.content)
    if result == "Index out of range":
        raise HTTPException(status_code=404, detail="Note not found")
    return NoteResponse(content=note.content, index=index)

@app.delete("/notes/{index}")
def delete_note(index: int):
    result = notes_app.del_note(index)
    if result == "Index out of range":
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)