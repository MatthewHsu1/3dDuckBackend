from fastapi import FastAPI
from app.api.v1.router import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="3D Duck Backend")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "3D Duck Backend is running"}

@app.get("/test")
def health_check():
    return {"status": "ok"}