import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    MaxLenLetter = int(os.getenv('MaxLenLetter', default=300))
    NumberQuestions = int(os.getenv('NumberQuestions', default=3))
    MaxNumberSkills = int(os.getenv('MaxNumberSkills', default=5))
    ApiKeyYndx = os.getenv('ApiKeyYndx')
    FolderIDYndx = os.getenv('FolderIDYndx')
    TemperatureYndx = os.getenv('TemperatureYndx', default=0.6)

    ApiAddrYndx = 'https://llm.api.cloud.yandex.net/llm/v1alpha/instruct'
