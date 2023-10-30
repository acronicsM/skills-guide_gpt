from enum import Enum

from pydantic import BaseModel, Field

from . import Proveders


Providers_enum = Enum(
        value='Providers',
        names=[(key, key) for key in Proveders],
    )


class Models(Enum):
    default = None
    gpt_35_turbo = 'gpt-3.5-turbo'
    gpt_4 = 'gpt-4'


class RequestModel(BaseModel):
    content: str = Field(description='Текст запроса к ChatGPT')
    model: Models = Field(description='Используемая модель GPT')
    provider: Providers_enum = Field(description='Провайдер у которого берем GPT')


class ResponseModel(BaseModel):
    result: str = Field(description='Ответ GPT')
