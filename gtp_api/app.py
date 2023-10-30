from fastapi import FastAPI

from .openai.router import router as openai_router
from .yandex.router import router as yandex_router

app = FastAPI(
    title='skills-guide_gpt'
)

app.include_router(openai_router)
app.include_router(yandex_router)
