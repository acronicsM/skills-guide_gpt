import json
from random import sample
from ..settings import Settings


def get_skills_text(skills: list):
    list_skills = list(set(skills))

    if len(list_skills) > Settings.MaxNumberSkills:
        return ', '.join(sample(list_skills, k=Settings.MaxNumberSkills))

    return ', '.join(list_skills)


def interview_response_to_dict(response: str):
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return dict()
