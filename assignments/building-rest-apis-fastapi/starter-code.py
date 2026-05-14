from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="Task Manager API")

# Task model
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory storage (in production, use a database)
tasks_db = []
next_id = 1

@app.get("/")
def read_root():
    return {"message": "Task Manager API"}

# TODO: Implement CRUD endpoints here

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)