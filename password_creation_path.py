from fastapi import APIRouter
from generator import generator_password


password_router = APIRouter(prefix="/create_password", tags=["create_password"])

@password_router.post("/generate_password")
async def create_password(password_length:int):
        created_password = generator_password(password_length)
        return {
                "password": created_password,
                "length": password_length
        }

