from fastapi import FastAPI
from models import Todo

app = FastAPI()

todos = []

# Get all todos
@app.get("/todos")
async def get_todos():
    return {'todos' : todos}

# Get a single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {'todo': todo}
    return {'message' : 'No Todo found'}


# Create a todo
@app.post("/todos")
async def create_todo(todo: Todo):
    todos.append(todo)
    return {'message' : 'Todo added successfully'}


# Update a todo
@app.put('/todos/{todo_id}')
async def update_todo(todo_id: int, new_item: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.item = new_item.item
            return {"message" : "Todo updated successfully"}
        return {'message': "No Todo found"}

# Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for item in todos:
        if item.id == todo_id:
            todos.remove(item)
            return {'message': 'item deleted successfully'}
    return {'message' : 'No Todo found'}