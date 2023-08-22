from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

# Get all todos
@app.get("/todos")
async def get_todos():
    return {'todos' : todos}

# Get a single todo

# Create a todo
@app.post("/todos")
async def create_todo(todo: Todo):
    todos.append(todo)
    return {'message' : 'item added successfully'}


# Update a todo

# Delete a todo