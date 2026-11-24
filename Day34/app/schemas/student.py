
from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Student's full name"
    )

    age: int = Field(
        ...,
        gt=0,
        le=100,
        description="Student's age (1 to 100)"
    )

    course: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Student's course name"
    )


class StudentUpdate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Updated student name"
    )

    age: int = Field(
        ...,
        gt=0,
        le=100,
        description="Updated student age (1 to 100)"
    )

    course: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Updated course name"
    )


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str
