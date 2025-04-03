from datetime import datetime
from thalentfrx.core.models.BaseModel import EntityMeta
from thalentfrx.core.models.AuditMixinModel import (
    AuditMixin,
)
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    Column,
    String,
    DateTime,
    Boolean,
)
import pytz
import bcrypt


class Users(EntityMeta, AuditMixin):
    __tablename__ = "auth_users"

    username: Mapped[str] = mapped_column(
        String(100), nullable=False, unique=True
    )
    password_hash: Mapped[str] = mapped_column(String(500), nullable=False)
    is_enabled = mapped_column(
        Boolean, nullable=False, default=True
    )
    is_logged: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    last_login: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime(1900, 1, 1, tzinfo=pytz.utc),
    )

    @property
    def password(self):
        # raise AttributeError('password not readable')
        pass

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")
