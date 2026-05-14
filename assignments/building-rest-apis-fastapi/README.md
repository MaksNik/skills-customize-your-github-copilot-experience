# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a REST API using the FastAPI framework to manage a collection of tasks. The API should support basic CRUD (Create, Read, Update, Delete) operations for task management.

## 📝 Tasks

### 🛠️ Set Up FastAPI Application

#### Description
Install FastAPI and create a basic application structure with a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn
- Create a FastAPI app instance
- Define a GET endpoint at "/" that returns {"message": "Task Manager API"}
- Run the server on localhost:8000

### 🛠️ Create Task Data Model

#### Description
Define a Pydantic model for Task items with fields like id, title, description, and completed status.

#### Requirements
Completed program should:

- Import BaseModel from Pydantic
- Create a Task model with appropriate fields
- Include type hints for all fields

### 🛠️ Implement CRUD Endpoints

#### Description
Create REST API endpoints for managing tasks: GET all tasks, GET single task, POST new task, PUT update task, DELETE task.

#### Requirements
Completed program should:

- GET /tasks: Return list of all tasks
- POST /tasks: Create new task and return it
- GET /tasks/{task_id}: Return specific task by ID
- PUT /tasks/{task_id}: Update existing task
- DELETE /tasks/{task_id}: Delete task by ID
- Use appropriate HTTP status codes
- Handle cases where task doesn't exist

### 🛠️ Add Request Validation

#### Description
Add input validation for creating and updating tasks using Pydantic models.

#### Requirements
Completed program should:

- Use different models for input (TaskCreate) and output (Task)
- Validate required fields
- Return appropriate error responses for invalid data

### 🛠️ Test the API

#### Description
Use tools like curl or a REST client to test all endpoints and ensure they work correctly.

#### Requirements
Completed program should:

- Demonstrate creating, reading, updating, and deleting tasks
- Show proper JSON responses
- Handle edge cases like non-existent IDs