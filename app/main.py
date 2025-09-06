from fastapi import FastAPI
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vrum Backend", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Vrum Backend API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
