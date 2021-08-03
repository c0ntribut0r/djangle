from environs import Env
from pathlib import Path

from starlette.staticfiles import StaticFiles
from starlette.routing import Route, Mount
from views import main

env = Env()

ROOT = Path(__file__).parent
DEBUG = env.bool('DEBUG', False)

STATIC_DIR = env.path('STATIC_DIR', str(ROOT.parent / 'data' / 'static'))
UPLOAD_DIR = env.path('UPLOAD_DIR', str(ROOT.parent / 'data' / 'upload'))

MIDDLEWARE = []

ROUTES = [
    Route('/', main, name='main'),
    Mount('/static', StaticFiles(directory=STATIC_DIR), name='static'),
]
