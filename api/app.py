import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from api.rate_limiter import setup_rate_limiting
from .routes import test
import config as conf

app = FastAPI(title="FastAPI Application", version="1.0.0")

setup_rate_limiting(app)

def runApp():

    api_router = APIRouter(prefix="/api")

    api_router.include_router(test.router)

    app.include_router(api_router)
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=conf.allowed_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    uvicorn.run(app, host=conf.server_address, port=conf.server_port)

def getApp():
    global app
    return app