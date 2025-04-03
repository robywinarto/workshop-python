import logging
import os

import uvicorn.logging
from fastapi import FastAPI

from thalentfrx.configs import Environment
from thalentfrx.configs.Logger import get_logger
from userapi.endpoint.restapi.metadata.Tags import Tags
from thalentfrx.helpers.fastapi import StartUpInfo
from thalentfrx.helpers.fastapi.ExceptionHandlers import add_unicorn_exception_handler
from userapi.router import include_router

# Core Application Instance
app = FastAPI(
    openapi_tags=Tags,
)

# Application Environment Configuration
env: Environment.EnvironmentSettings = (
    Environment.get_environment_variables()
)
# basedir = path of module userapi
basedir: str = os.path.abspath(os.path.dirname(__file__))
environment: str = os.getenv("ENV")

# Logger
logger: logging.Logger = get_logger(__name__)
uvicorn_logger: logging.Logger = logging.getLogger(
    "uvicorn.error"
)

# Add Env
app.environment = environment
app.basedir = basedir

# Add Config
app.env = env

# Add Logger
app.logger = logger
app.uvicorn_logger = uvicorn_logger

app.title = env.APP_NAME
app.version = env.API_VERSION
app.debug = env.DEBUG_MODE

# Add error handler
add_unicorn_exception_handler(app)

# Add routers REST API
include_router(app=app)

# Show startup info
StartUpInfo.show_startup_info(app, app.logger)
# Show startup info (ONLY SHOW ON UVICORN CONSOLE)
# StartUpInfo.show_startup_info(app, app.uvicorn_logger)

# if directly on app.py not as module, will run below script
if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p",
        "--port",
        default=5000,
        type=int,
        help="port to listen on",
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        type=str,
        help="host to listen on",
    )
    parser.add_argument(
        "--loglevel",
        default="debug",
        type=str,
        help="log level",
    )
    parser.add_argument(
        "--workers", default=1, type=int, help="log level"
    )

    args = parser.parse_args()
    port = args.port
    host = args.host
    log_level = args.loglevel
    workers = args.workers

    uvicorn.run(
        app,
        host=host,
        port=port,
        log_level=log_level,
        workers=workers,
    )
