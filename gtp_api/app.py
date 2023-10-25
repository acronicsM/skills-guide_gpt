from fastapi import FastAPI

from .routers import router

app = FastAPI(
    title='skills-guide_gpt'
)

app.include_router(router)
