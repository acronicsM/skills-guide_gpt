from fastapi import APIRouter

from .services_model.get_models import get_cover_letter, get_interview
from .schemas import LetterResponseModel, LetterModel, InterviewResponseModel, InterviewModel

router = APIRouter(
    prefix='/gpt',
    tags=['GPT'],
)


@router.post(path="/letter",
             response_model=LetterResponseModel,
             name='Сопроводительное письмо',
             description='Возвращает сформированное сопроводительное письмо')
async def letter(query: LetterModel):
    return await get_cover_letter(**query.model_dump())


@router.post(path="/interview",
             response_model=InterviewResponseModel,
             name='Возможные вопросы на собеседовании',
             description='Возвращает !!!'
             )
async def interview(query: InterviewModel):
    return await get_interview(**query.model_dump())
