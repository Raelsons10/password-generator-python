from fastapi import FastAPI

app = FastAPI()

from password_creation_path import password_router

app.include_router(password_router)

@app.get("/")
def test_api():
    
    return {"message": "Password Generator API"}

