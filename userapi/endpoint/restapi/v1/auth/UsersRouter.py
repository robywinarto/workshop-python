
# Python class for restapi router AuthUsers
# Created on 2025-01-16 ( Time 12:55:02 )

from typing import Any, List, Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from thalentfrx.core.entities.PageRecord import PageRecord
from thalentfrx.db.session_manager import (
    get_db_session,
)

from userapi.endpoint.restapi.schemas.auth.UsersSchema import (
    UsersCreateSchema,
    UsersSchema,
    UsersListSchema,
    UsersUpdateSchema,
)
from userapi.entities.auth.UsersEntity import UsersEntity
from thalentfrx.helpers.fastapi.AuthHelper import auth_check, auth_info
from thalentfrx.helpers.fastapi.ExceptionHandlers import http_exception_handler
from userapi.services.auth.UsersDto import (
    CreateRequestDto,
    UpdateRequestDto,
    SoftDeleteRequestDto,
    RestoreRequestDto,
)
from userapi.services.auth.UsersService import UsersService
from thalentfrx.core.entities.ListParam import ListParam
from thalentfrx.core.entities.PagingParam import PagingParam
from thalentfrx.core.endpoint.rest_api.CommonSchema import ListParamSchema, PagingParamSchema

UsersRouter = APIRouter(prefix="/v1/users", tags=["Users"])


@UsersRouter.post(
    "/list",
    status_code=status.HTTP_200_OK,
    response_model=UsersListSchema,
    dependencies=[Depends(auth_check)]
)
@http_exception_handler()
def index(
        param: ListParamSchema,
        session: Session = Depends(get_db_session),
) -> Any:
    service: UsersService = UsersService(session)

    data: ListParam = ListParam().model_copy(update=param.model_dump())
    page_entity: PageRecord[UsersEntity] = service.list(data)
    return page_entity


@UsersRouter.post(
    "/paging",
    status_code=status.HTTP_200_OK,
    response_model=UsersListSchema,
    dependencies=[Depends(auth_check)]
)
@http_exception_handler()
def paging(
        param: PagingParamSchema,
        session: Session = Depends(get_db_session),
) -> Any:
    service: UsersService = UsersService(session)

    data: PagingParam = PagingParam().model_copy(update=param.model_dump())
    page_entity: PageRecord[UsersEntity] = service.paging(data)
    return page_entity


@UsersRouter.get(
    "/{entity_id}",
    status_code=status.HTTP_200_OK,
    response_model=UsersSchema,
    dependencies=[Depends(auth_check)]
)
@http_exception_handler()
def get(
        entity_id: str, session: Session = Depends(get_db_session)
) -> Any:
    service: UsersService = UsersService(session)
    entity: UsersEntity = service.get(entity_id)
    return entity


@UsersRouter.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UsersSchema,
    dependencies=[Depends(auth_check)]
)
@http_exception_handler()
def create(
        post_data: UsersCreateSchema,
        auth: Annotated[tuple[str, List[str]], Depends(auth_info)],
        session: Session = Depends(get_db_session),
) -> Any:
    identity: str = auth[0]
    authorize_scope: List[str] = auth[1]

    service: UsersService = UsersService(session)
    data: CreateRequestDto = CreateRequestDto(
        created_by=identity,
        username=post_data.username,
        password_hash=post_data.password_hash,
        is_enabled=post_data.is_enabled,
        is_logged=post_data.is_logged,
        last_login=post_data.last_login,
    )
    entity: UsersEntity = service.create(data)
    return entity


@UsersRouter.patch(
    "/{entity_id}",
    status_code=status.HTTP_200_OK,
    response_model=UsersSchema,
    dependencies=[Depends(auth_check)]
)
@http_exception_handler()
def update(
        entity_id: str,
        post_data: UsersUpdateSchema,
        auth: Annotated[tuple[str, List[str]], Depends(auth_info)],
        session: Session = Depends(get_db_session),
) -> Any:
    identity: str = auth[0]
    authorize_scope: List[str] = auth[1]

    service: UsersService = UsersService(session)
    data: UpdateRequestDto = UpdateRequestDto(
        updated_by=identity,
        id=entity_id,
        username=post_data.username,
        password_hash=post_data.password_hash,
        is_enabled=post_data.is_enabled,
        is_logged=post_data.is_logged,
        last_login=post_data.last_login,
    )
    entity: UsersEntity = service.update(data)
    return entity


@UsersRouter.delete(
    "/{entity_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(auth_check)]
)
@http_exception_handler()
def delete(
        entity_id: str, session: Session = Depends(get_db_session)
) -> None:
    service: UsersService = UsersService(session)
    service.delete(entity_id)


@UsersRouter.patch(
    "/{entity_id}/softdelete",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(auth_check)]
)
@http_exception_handler()
def soft_delete(
        entity_id: str,
        auth: Annotated[tuple[str, List[str]], Depends(auth_info)],
        session: Session = Depends(get_db_session)
) -> None:
    identity: str = auth[0]
    authorize_scope: List[str] = auth[1]

    data: SoftDeleteRequestDto = SoftDeleteRequestDto(
        id=entity_id,
        updated_by=identity,
    )

    service: UsersService = UsersService(session)
    service.soft_delete(data)


@UsersRouter.patch(
    "/{entity_id}/restore",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(auth_check)]
)
@http_exception_handler()
def restore(
        entity_id: str,
        auth: Annotated[tuple[str, List[str]], Depends(auth_info)],
        session: Session = Depends(get_db_session)
) -> None:
    identity: str = auth[0]
    authorize_scope: List[str] = auth[1]

    data: RestoreRequestDto = RestoreRequestDto(
        id=entity_id,
        updated_by=identity,
    )

    service: UsersService = UsersService(session)
    service.restore(data)
