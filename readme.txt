# Students CRUD API

pip install -r requirements.txt
uvicorn main:app --reload

## Students

The in-memory Students API supports:

- `POST /students` to create a student
- `GET /students` to list students
- `GET /students/{student_id}` to retrieve a student
- `PUT /students/{student_id}` to replace a student
- `DELETE /students/{student_id}` to delete a student

Create and update requests accept `name`, `email`, `course`, and `semester`.
