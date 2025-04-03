
# Python class for repository AuthUsers
# Created on 2025-01-16 ( Time 12:55:02 )

from typing import Optional

from sqlalchemy.orm import Session
from thalentfrx.core.entities.PageRecord import PageRecord
from thalentfrx.core.repositories.BaseRepository import (
    BaseRepository,
)

from userapi.configs.db.models.auth.UsersModel import Users
from userapi.entities.auth.UsersEntity import UsersEntity
from thalentfrx.core.entities.ListParam import ListParam

from thalentfrx.core.entities.PagingParam import PagingParam



class UsersRepository(BaseRepository[Users]):

    def __init__(self, session: Session) -> None:
        super().__init__(Users, session)

    def list_of_entity(
        self,
        param: Optional[ListParam],
    ) -> PageRecord[UsersEntity]:

        data: PageRecord[UsersEntity] = PageRecord[
            UsersEntity
        ](count=0, rows=[])

        result: PageRecord[Users] = super()._list(list_param=param)

        data.count = result.count
        data.rows = [
            UsersEntity().model_copy(update=row.to_dict())
            for row in result.rows
        ]

        return data

    def paging_of_entity(
        self,
        param: Optional[PagingParam],
    ) -> PageRecord[UsersEntity]:

        data: PageRecord[UsersEntity] = PageRecord[
            UsersEntity
        ](count=0, rows=[])

        result: PageRecord[Users] = super()._paging(paging_param=param)

        data.count = result.count
        data.rows = [
            UsersEntity().model_copy(update=row.to_dict())
            for row in result.rows
        ]

        return data

    def get_entity(self, entity_id: str) -> UsersEntity:

        model: Users = super()._get(entity_id)

        if model:
            return UsersEntity().model_copy(update=model.to_dict())
        else:
            return UsersEntity()

    def create_entity(
        self,
        entity: UsersEntity,
        is_transaction: bool = False,
    ) -> None:

        model: Users = Users(**entity.model_dump(exclude_unset=True))
        return super()._create(model, is_transaction)

    def modify_entity(
        self,
        entity: UsersEntity,
        is_transaction: bool = False,
    ) -> None:

        model: Users = Users(**entity.model_dump(exclude_unset=True))
        return super()._update(str(model.id), model, is_transaction)

    def delete_entity(
        self,
        entity_id: str,
        is_transaction: bool = False,
    ) -> None:
        return super()._delete(entity_id, is_transaction)
