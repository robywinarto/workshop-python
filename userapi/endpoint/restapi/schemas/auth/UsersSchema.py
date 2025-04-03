
# Python class for restapi schema AuthUsers
# Created on 2025-01-16 ( Time 12:55:02 )

from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional


class UsersCreateSchema(BaseModel):
    username: str = Field(min_length=1, max_length=100)
    password_hash: str = Field(min_length=1, max_length=500)
    is_enabled: bool
    is_logged: bool
    last_login: datetime

class UsersUpdateSchema(BaseModel):
    id: str
    username: str = Field(min_length=1, max_length=100)
    password_hash: str = Field(min_length=1, max_length=500)
    is_enabled: bool
    is_logged: bool
    last_login: datetime

class UsersSchema(BaseModel):
    username: Optional[str] = None
    password_hash: Optional[str] = None
    is_enabled: Optional[bool] = None
    is_logged: Optional[bool] = None
    last_login: Optional[datetime] = None
    id: Optional[str] = None
    is_deleted: Optional[bool] = None
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    row_version: Optional[str] = None
    row_timespan: Optional[int] = None

class UsersListSchema(BaseModel):
    count: Optional[int] = Field(default=0)
    rows: Optional[List[UsersSchema]] = Field(default=[])