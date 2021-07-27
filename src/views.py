
from fastapi import Request
from starlette.responses import Response

from templates import templates


async def main(request: Request) -> Response:
    return templates.TemplateResponse('main.html', {'request': request})
