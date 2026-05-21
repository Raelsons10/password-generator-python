from pydantic import BaseModel, Field

class PasswordRequest(BaseModel):
    length: int = Field(default=12, ge=12, description="A senha deve ser maior ou igual a 12 caracteres.")

