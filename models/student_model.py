from pydantic import BaseModel, EmailStr

class CreateStudent(BaseModel):
    name: str
    marks: float
    course: str

class Student(BaseModel):
    id: int
    name: str
    marks: float
    course: str