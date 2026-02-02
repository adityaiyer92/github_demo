import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="To-Do List API")

todo_list: List[str] = []

# Define Models
class TodoItem(BaseModel):
    item: str

class DownloadRequest(BaseModel):
    filename: str | None = None

# Define Endpoints

@app.get("/todo")
def view_list():
    """Displays the current to-do list."""
    return {"todo_list": todo_list,
            "count": len(todo_list)}

@app.post("/todo")
def add_item(payload: TodoItem):
    """Adds a new item to the to-do list."""
    todo_list.append(payload.item)
    return{
        "message": "To-do item added successfully.",
        "items": todo_list
    }

@app.delete("/todo/{item_number}")
def mark_completed(item_number: int):
    """Marks an item as completed (removes it from the list)."""
    try:
        if 1 <= item_number <= len(todo_list):
            removed_item = todo_list.pop(item_number - 1)
            return {
                "message": f"'{removed_item}' has been marked as completed.",
                "items": todo_list
            }
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid item number")

@app.post("/todo/download")
def download_list(payload: DownloadRequest):
    """Downloads the to-do list to a text file."""
    filename = payload.filename or "saved_lists/todo_list.txt"

    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as file:
            for item in todo_list:
                file.write(f"{item}\n")
        return {
            "message": f"Saved to {filename}"
        }
    except IOError as e:
        raise HTTPException(status_code=500, detail=str(e))