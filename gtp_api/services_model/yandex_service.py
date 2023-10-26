import json

import aiohttp

from . import Parser, ServicesModel
from ..settings import Settings


class YandexGPT(Parser, ServicesModel):
    LetterInstr = 'Ты соискатель на должность которому нужно написать сопроводительное письмо'
    InterviewInstrRequests = 'Ты tech lead python который проводит собеседование'
    InterviewInstrResponse = 'Ты tech lead python который отвечает на вопросы python junior"'
    InterviewQuestion = 'Задай технический вопрос по flask'

    @classmethod
    async def __get_answer_gpt(cls, content, provider=None, model=None):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Api-Key {Settings.ApiKeyYndx}',
            'x-folder-id': Settings.FolderIDYndx,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(Settings.ApiAddrYndx, headers=headers, data=json.dumps(content)) as response:
                answer = await response.json()

        return answer['result']['alternatives'][0]['text']

    @classmethod
    async def letter(cls, description, provider=None, model=None):
        content = {
            "model": 'general',
            "instruction_text": cls.LetterInstr,
            "request_text": description,
            "generation_options": {
                "max_tokens": 2500,
                "temperature": 0.6
            }
        }

        return await cls.__get_answer_gpt(content=content)

    @classmethod
    async def interview(cls, key_skills, basic_skills, provider, model):
        content = {
            "model": 'general',
            "instruction_text": cls.InterviewInstrRequests,
            "request_text": key_skills,
            "generation_options": {
                "max_tokens": 2500,
                "temperature": 0.6
            }
        }

        return await cls.__get_answer_gpt(content=content)
