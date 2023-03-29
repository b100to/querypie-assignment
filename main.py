from fastapi import FastAPI
from controllers import router as env_vars_router

app = FastAPI()

app.include_router(env_vars_router, prefix="/api")
