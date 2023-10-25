from .chatgtp_service import ChatGPT
from .yandex_service import YandexGPT

SERVICES = {
        'yandex': YandexGPT,
        'chatgpt': ChatGPT,
    }


def get_cover_letter(service, model, provider, description):
    return {'result': SERVICES[service.value].letter(description=description, provider=provider, model=model)}


def get_interview(service, model, provider, key_skills, basic_skills):
    return {'result': SERVICES[service.value].interview(key_skills=key_skills,
                                                        basic_skills=basic_skills,
                                                        provider=provider,
                                                        model=model)
            }
