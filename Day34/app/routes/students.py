
from typing import List

from fastapi import APIRouter, HTTPException, status

from app.schemas.student import (
    StudentCreate,
    StudentUpdate,
    StudentResponse
)

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

# Temporary in-memory storage
students = {}
next_id = 1


@router.get(
    "/",
    response_model=List[StudentResponse],
    summary="View All Students",
    description="Retrieve a list of all registered students."
)
def get_students():
    return list(students.values())


@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Add New Student",
    description="Create a new student record with validated information."
)
def add_student(student: StudentCreate):
    global next_id

    new_student = {
        "id": next_id,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

    students[next_id] = new_student
    next_id += 1

    return new_student


@router.get(
    "/search",
    response_model=List[StudentResponse],
    summary="Search Student",
    description="Search students by their name."
)
def search_student(name: str):
    results = [
        student
        for student in students.values()
        if name.lower() in student["name"].lower()
    ]

    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No student found with the provided name."
        )

    return results


@router.get(
    "/{student_id}",
    response_model=StudentResponse,
    summary="Get Student by ID",
    description="Retrieve details of a specific student."
)
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found."
        )

    return students[student_id]


@router.put(
    "/{student_id}",
    response_model=StudentResponse,
    summary="Update Student",
    description="Update all information for an existing student."
)
def update_student(student_id: int, student: StudentUpdate):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found."
        )

    updated_student = {
        "id": student_id,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

    students[student_id] = updated_student

    return updated_student


@router.delete(
    "/{student_id}",
    summary="Delete Student",
    description="Delete a student record using its ID."
)
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found."
        )

    del students[student_id]

    return {
        "message": "Student deleted successfully.",
        "student_id": student_id
    }
