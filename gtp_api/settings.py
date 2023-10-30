import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    ApiKeyYndx = os.getenv('ApiKeyYndx')
    FolderIDYndx = os.getenv('FolderIDYndx')
    TemperatureYndx = float(os.getenv('TemperatureYndx', default=0.6))

    ApiAddrYndx = 'https://llm.api.cloud.yandex.net/llm/v1alpha/instruct'
