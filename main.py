from fastapi import FastAPI
from routers.student_routes import router

app = FastAPI(title="Students CRUD API")

app.include_router(router)