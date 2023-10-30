from pydantic import BaseModel, Field


class RequestModel(BaseModel):
    content: str = Field(description='Текст запроса к YandexGPT')
    instruction: str | None = Field(description='Предварительное текстовое условие или контекст запроса.')


class ResponseModel(BaseModel):
    result: str = Field(description='Ответ GPT')
