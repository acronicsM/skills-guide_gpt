from . import Parser, ServicesModel


class YandexGPT(Parser, ServicesModel):
    @classmethod
    def __get_answer_gpt(cls, content, provider=None, model=None):
        return 'coming soon'

    @classmethod
    def letter(cls, description, provider=None, model=None):
        content = f'{cls.LetterPrefix}\n{description}'
        return cls.__get_answer_gpt(content=content, provider=provider, model=model)

    @classmethod
    def interview(cls, key_skills, basic_skills, provider, model):
        description = 'fgfgf'
        content = f'{cls.LetterPrefix}\n{description}'
        return cls.__get_answer_gpt(content=content, provider=provider, model=model)
