import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    MaxLenLetter = int(os.getenv('MaxLenLetter', default=300))
    NumberQuestions = int(os.getenv('NumberQuestions', default=3))
    MaxNumberSkills = int(os.getenv('MaxNumberSkills', default=5))
