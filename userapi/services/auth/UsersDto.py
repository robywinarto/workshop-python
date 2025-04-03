
# Python class for dto AuthUsers
# Created on 2025-01-16 ( Time 12:55:02 )

from pydantic import BaseModel, Field
from datetime import datetime


class CreateRequestDto(BaseModel):
    created_by: str
    username: str = Field(min_length=1, max_length=100)
    password_hash: str = Field(min_length=1, max_length=500)
    is_enabled: bool
    is_logged: bool
    last_login: datetime


class UpdateRequestDto(BaseModel):
    updated_by: str
    id: str
    username: str = Field(min_length=1, max_length=100)
    password_hash: str = Field(min_length=1, max_length=500)
    is_enabled: bool
    is_logged: bool
    last_login: datetime


class SoftDeleteRequestDto(BaseModel):
    updated_by: str
    id: str


class RestoreRequestDto(BaseModel):
    updated_by: str
    id: str
