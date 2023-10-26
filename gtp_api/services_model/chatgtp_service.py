from g4f import ChatCompletion
from g4f.models import gpt_35_turbo
from g4f.Provider import GPTalk

from . import Parser, ServicesModel
from ..settings import Settings
from ..utils.interview import get_skills_text, interview_response_to_dict


class ChatGPT(Parser, ServicesModel):
    LetterPrefix = f'Напиши сопроводительное письмо не длиннее {Settings.MaxLenLetter} символов для вакансии:'
    InterviewPrefix = f'Придумай по %number% вопроса для собеседования с ответами для каждого hard skill:'

    QuestionAnswer = '''Оформи в виде python структуры 
        [
          {
            "skill": "string",
            "qna": [
              {
                "question": "string",
                "answer": "string"
              }
            ]
          }
        '''

    @classmethod
    async def __get_answer_gpt(cls, content, provider=None, model=None):
        m = model if model else gpt_35_turbo
        p = provider if provider else GPTalk
        p = None
        response = await ChatCompletion.create_async(
            model=m,
            messages=[{"role": "user", "content": content}],
            provired=p,
        )

        return response

    @classmethod
    async def letter(cls, description, provider, model):
        content = f'{cls.LetterPrefix}\n{description}'
        return await cls.__get_answer_gpt(content=content, provider=provider, model=model)

    @classmethod
    async def interview(cls, key_skills, basic_skills, provider, model):
        pref = cls.InterviewPrefix.replace('%number%', str(Settings.NumberQuestions))
        skills_text = get_skills_text(basic_skills + key_skills)

        basic_qna = await cls.__get_answer_gpt(
            content=f'{pref} {skills_text}\n{cls.QuestionAnswer}',
            provider=provider,
            model=model)

        response = interview_response_to_dict(basic_qna)

        return response
