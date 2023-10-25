import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    MaxLenLetter = os.getenv('MaxLenLetter', default=300)
    NumberQuestions = os.getenv('NumberQuestions', default=3)
    NumberBasicQuestions = os.getenv('NumberBasicQuestions', default=5)
