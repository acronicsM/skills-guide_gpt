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
    LetterPrefix = f'Напиши сопроводительное письмо не длиннее {Settings.MaxLenLetter} символов для вакансии:'
    QuestionAnswer = 'Оформи в виде списка словарей Python, ключи словаря "вопрос", "ответ"'
    InterviewPrefix = f'Придумай {Settings.NumberQuestions} вопроса по %skill% для собеседования с ответами'
    InterviewBasicPrefix = f'Придумай {Settings.NumberBasicQuestions} технический вопроса по %skill% для собеседования с ответами'



