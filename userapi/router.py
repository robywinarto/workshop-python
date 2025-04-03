from fastapi import FastAPI

from userapi.endpoint.restapi.v1.auth.UsersRouter import UsersRouter

def include_router(app: FastAPI):
    app.include_router(UsersRouter)