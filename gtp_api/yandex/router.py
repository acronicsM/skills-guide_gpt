from fastapi import APIRouter

from .models import get_answer
from .schemas import ResponseModel, RequestModel

router = APIRouter(
    prefix='/yandex',
    tags=['Yandex'],
)


@router.post(path="/answer",
             response_model=ResponseModel,
             name='Ответ GPT',
             description='Возвращает ответ GPT')
async def answer(query: RequestModel):
    result = await get_answer(**query.model_dump())
    return {'result': result}
