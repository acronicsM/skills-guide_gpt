from g4f import ChatCompletion
from g4f.models import gpt_35_turbo
from g4f.Provider import GPTalk

from . import Parser, ServicesModel


class ChatGPT(Parser, ServicesModel):
    @classmethod
    def __get_answer_gpt(cls, content, provider=None, model=None):

        m = model if model else gpt_35_turbo
        p = provider if provider else GPTalk
        response = ChatCompletion.create(
            model=m,
            messages=[{"role": "user", "content": content}],
            provired=p,
        )

        return response

    @classmethod
    def letter(cls, description, provider, model):
        content = f'{cls.LetterPrefix}\n{description}'
        return cls.__get_answer_gpt(content=content, provider=provider, model=model)

    @classmethod
    def interview(cls, key_skills, basic_skills, provider, model):

        for skill in key_skills:
            if skill in basic_skills:
                pass
            else:
                pass

        description = 'fgfgf'
        content = f'{cls.LetterPrefix}\n{description}'
        return cls.__get_answer_gpt(content=content, provider=provider, model=model)
