# Day 34 – Student Management REST API

## Project Overview
This project is a Student Management REST API developed using FastAPI and Python. It allows users to add, view, search, update, and delete student records.

The project uses an in-memory dictionary for temporary data storage. No database is used.

## Technologies Used
- Python
- FastAPI
- Pydantic
- Uvicorn
- Swagger UI

## What is a REST API?
A REST API allows different applications to communicate with each other using HTTP methods. It uses methods such as GET, POST, PUT, and DELETE to perform operations on data.

## Difference Between GET and POST
- **GET:** Retrieves data from the server.
- **POST:** Sends new data to the server to create a resource.

Other methods used:
- **PUT:** Updates an existing student.
- **DELETE:** Deletes a student.

## What is Pydantic?
Pydantic is a Python library used for data validation. In this project, it validates student information such as name, age, and course before accepting a request.

Validation rules:
- Name: 2–50 characters
- Age: Greater than 0 and maximum 100
- Course: 2–50 characters

## Project Structure
```text
Day34/
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── students.py
│   └── schemas/
│       └── student.py
├── requirements.txt
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Welcome message |
| GET | /health | API health check |
| GET | /students/ | View all students |
| POST | /students/ | Add a student |
| GET | /students/search?name=Saba | Search students by name |
| GET | /students/{student_id} | Get a student by ID |
| PUT | /students/{student_id} | Update student information |
| DELETE | /students/{student_id} | Delete a student |

## Example Request – Add Student

POST `/students/`

```json
{
  "name": "Saba Noor",
  "age": 22,
  "course": "Python"
}
```

Example response:

```json
{
  "id": 1,
  "name": "Saba Noor",
  "age": 22,
  "course": "Python"
}
```

## Error Handling
The API returns appropriate error messages when a student is not found. Pydantic also returns validation errors when incoming data does not meet the required rules.

## Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
python -m uvicorn app.main:app --reload
```

Open the following URLs:

- API: http://127.0.0.1:8000/
- Swagger UI: http://127.0.0.1:8000/docs
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

## Data Storage
Student records are stored temporarily in an in-memory Python dictionary. Data resets when the application restarts.

## Learning Outcomes
- Understanding REST API fundamentals
- Creating API endpoints using FastAPI
- Using Pydantic for request validation
- Testing APIs through Swagger UI
- Organizing code using routes and schemas