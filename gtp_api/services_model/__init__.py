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
