
# Python class for service AuthUsers
# Created on 2025-01-16 ( Time 12:55:02 )

import uuid

from sqlalchemy.orm import Session
from thalentfrx.core.services.BaseService import BaseService

from userapi.entities.auth.UsersEntity import UsersEntity
from userapi.repositories.auth.UsersRepository import UsersRepository
from userapi.services.auth.UsersDto import (
    CreateRequestDto,
    UpdateRequestDto,
    SoftDeleteRequestDto,
    RestoreRequestDto,
)


class UsersService(BaseService[UsersEntity, UsersRepository]):

    def __init__(self, session: Session) -> None:
        super().__init__(UsersRepository(session))

    def create(self, dto: CreateRequestDto) -> UsersEntity:
        entity_id: uuid = uuid.uuid4()
        entity: UsersEntity = UsersEntity(
            created_by=dto.created_by,
            id=str(entity_id),
            username=dto.username,
            password_hash=dto.password_hash,
            is_enabled=dto.is_enabled,
            is_logged=dto.is_logged,
            last_login=dto.last_login,
        )
        self.repo.create_entity(entity)
        return self.repo.get_entity(str(entity_id))

    def update(self, dto: UpdateRequestDto) -> UsersEntity:
        entity: UsersEntity = UsersEntity(
            updated_by=dto.updated_by,
            id=dto.id,
            username=dto.username,
            password_hash=dto.password_hash,
            is_enabled=dto.is_enabled,
            is_logged=dto.is_logged,
            last_login=dto.last_login,
        )
        self.repo.modify_entity(entity)
        return self.repo.get_entity(dto.id)

    def soft_delete(self, dto: SoftDeleteRequestDto) -> UsersEntity:
        entity: UsersEntity = UsersEntity(
            updated_by=dto.updated_by,
            id=dto.id,
            is_deleted=True
        )
        self.repo.modify_entity(entity)
        return self.repo.get_entity(dto.id)

    def restore(self, dto: RestoreRequestDto) -> UsersEntity:
        entity: UsersEntity = UsersEntity(
            updated_by = dto.updated_by,
            id=dto.id,
            is_deleted=False
        )
        self.repo.modify_entity(entity)
        return self.repo.get_entity(dto.id)
