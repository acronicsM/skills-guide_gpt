from abc import ABC, abstractmethod

from gtp_api.settings import Settings


class Parser(ABC):
    @classmethod
    @abstractmethod
    def __get_answer_gpt(cls, content, provider, model):
        pass

    @classmethod
    @abstractmethod
    def letter(cls, content, provider, model):
        pass

    @classmethod
    @abstractmethod
    def interview(cls, key_skills, basic_skills, provider, model):
        pass


class ServicesModel:
    LetterInstructionYndx = 'Ты соискатель на должность которому нужно написать сопроводительное письмо'

