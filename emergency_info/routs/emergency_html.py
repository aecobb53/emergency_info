from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from html import project_base_page, base_emergency_html_page, unimplemented_page

e_router = APIRouter(
    prefix='/e',
    tags=['emergency'],
)
emergency_router = APIRouter(
    prefix='/emergency',
    tags=['emergency'],
)


@e_router.get('/', status_code=200)
@emergency_router.get('/', status_code=200)
async def emergency_base_page():
    # emergency_base_page = unimplemented_page()
    emergency_base_page = base_emergency_html_page()
    return HTMLResponse(content=emergency_base_page)