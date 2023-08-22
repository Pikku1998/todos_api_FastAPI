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
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for item in todos:
        if item.id == todo_id:
            return {'todo': item}
    return {'message' : 'No item found'}


# Create a todo
@app.post("/todos")
async def create_todo(todo: Todo):
    todos.append(todo)
    return {'message' : 'item added successfully'}


# Update a todo

# Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for item in todos:
        if item.id == todo_id:
            todos.remove(item)
            return {'message': 'item deleted successfully'}
    return {'message' : 'No item found'}