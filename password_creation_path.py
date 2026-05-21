from fastapi import APIRouter, HTTPException
from generator import generator_password
from utils import is_valid_password_length


password_router = APIRouter(prefix="/create_password", tags=["create_password"])

@password_router.post("/generate_password")
async def create_password(password_length:int):
        if not is_valid_password_length(password_length):
                raise HTTPException(
                        status_code=422,
                        detail="A senha deve conter no mínimo 12 caracteres."
                )
        created_password = generator_password(password_length)
        return {
                "password": created_password,
                "length": password_length
        }



