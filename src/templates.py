from fastapi.templating import Jinja2Templates
from pathlib import Path


templates = Jinja2Templates(directory=Path(__file__).parent / 'templates')
