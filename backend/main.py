from fastapi import FastAPI
from routers import auth, resume, analysis

app = FastAPI()

app.include_router(auth.router)
app.include_router(resume.router)
app.include_router(analysis.router)
