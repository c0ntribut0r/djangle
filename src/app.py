from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.routing import Route, Mount
from settings import DEBUG, STATIC_DIR
from views import main


app = Starlette(
    debug=DEBUG,
    routes=[
        Route('/', main, name='main'),
        Mount('/static', StaticFiles(directory=STATIC_DIR), name='static'),
    ],
)
