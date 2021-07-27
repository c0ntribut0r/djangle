from fastapi import FastAPI
from starlette.routing import Route
from fastapi.responses import HTMLResponse

from database import db_connect, db_disconnect
from views import main


app = FastAPI(
    on_startup=[db_connect],
    on_shutdown=[db_disconnect],
    default_response_class=HTMLResponse,
    routes=[
        Route('/', endpoint=main),
    ]
)
