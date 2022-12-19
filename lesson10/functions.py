# Импорт JSON
import json


# Функция, загружающая данные из файла
def load_candidates():
    with open("candidates.json", "r", encoding="utf-8") as file:
        list_candidates = json.load(file)
    return list_candidates


# Функция, показывающая всех кандидатов
def get_all():
    candidates = load_candidates()
    for candidate in candidates:
        print(candidate['name'])


# Функция, возвращающая кандидата по pk
def get_by_pk(pk):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate


# Функция, возвращающая кандидатов по навыку
def get_by_skill(skill_name):
    candidates = load_candidates()
    candidates_with_skills = []
    for candidate in candidates:
        skills = candidate['skills'].split(", ")
        for skill in skills:
            if str(skill_name).lower() == skill.lower():
                candidates_with_skills.append(candidate)
    return candidates_with_skills
