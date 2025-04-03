
# Python class for entity AuthUsers
# Created on 2025-01-16 ( Time 12:55:02 )

from datetime import datetime
from typing import Optional
import pytz
from thalentfrx.core.entities.BaseEntity import BaseEntity


class UsersEntity(BaseEntity):
    password: Optional[str] = ""
    username: Optional[str] = ""
    password_hash: Optional[str] = ""
    is_enabled: Optional[bool] = False
    is_logged: Optional[bool] = False
    last_login: Optional[datetime] = datetime(1900, 1, 1, tzinfo=pytz.utc)
