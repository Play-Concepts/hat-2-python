from fastapi import FastAPI, HTTPException

from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from app.core import auth
from app.routes import data_route


async def http_exception_handler(request, exception):
    return JSONResponse(
        status_code=exception.status_code,
        content=exception.detail
    )

app = FastAPI(exception_handlers={
    HTTPException: http_exception_handler
})

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(data_route.router)
