from enum import Enum

from pydantic import BaseModel, Field

from .services_model.get_models import SERVICES


class GPTModel(BaseModel):
    service: Enum(
        value='BugStatus',
        names=[(k.upper(), k) for k, v in SERVICES.items()],
    ) = Field(description='Яндекс или ChatGPT')
    model: str | None = Field(description='Используемая версия GPT, используется только для сервиса chatgp')
    provider: str | None = Field(description='Провайдер у которого берем GPT, используется только для сервиса chatgpt')


class LetterModel(GPTModel):
    description: str = Field(description='Описание вакансии')


class LetterResponseModel(BaseModel):
    result: str = Field(description='Сопроводительное письмо')


class InterviewModel(GPTModel):
    key_skills: list[str] = Field(description='Навыки вакансии')
    basic_skills: list[str] = Field(description='Базовые навыки вакансии')


class InterviewQnA(BaseModel):
    question: str
    answer: str


class InterviewSkill(BaseModel):
    skill: str
    qna: list[InterviewQnA]


class InterviewResponseModel(BaseModel):
    result: list[InterviewSkill]
