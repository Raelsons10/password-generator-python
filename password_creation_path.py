from fastapi import APIRouter
from generator import generator_password
from schemas import PasswordRequest

password_router = APIRouter(prefix="/create_password", tags=["create_password"])

@password_router.post("/generate_password")
async def create_password(request: PasswordRequest):
        generated_password = generator_password(request.length)
        return {
                "password": generated_password,
                "length": request.length
        }


