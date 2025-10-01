from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Lifecycle Demo")

app.include_router(router)
