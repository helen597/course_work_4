import json, os
from src.vacancy import Vacancy
from src.JSON_processor import JSONSaver


def filter_vacancies(hh_vacancies, superjob_vacancies, filter_words):
    """Функция, фильтрующая вакансии с сайтов hh и superjob"""
    new_list = []
    filter_words = set(filter_words)
    punc = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

    if os.path.exists('filtered.json'):
        with open('filtered.json', 'w', encoding='utf-8') as f:
            json.dump(new_list, f, ensure_ascii=False)

    with open(hh_vacancies, 'r', encoding='utf-8') as f:
        content = json.load(f)

    # Цикл по вакансиям hh
    for vacancy in content:

        requirements = vacancy['requirements']
        if requirements is None:
            requirements = set()
        else:
            for s in requirements:
                if s in punc:
                    new_str = requirements.replace(s, "")
            requirements = set(new_str.lower().split())

        description = vacancy['description']
        if description is None:
            description = set()
        else:
            for s in description:
                if s in punc:
                    new_str = description.replace(s, "")
            description = set(new_str.lower().split())

        if filter_words.intersection(requirements.union(description)) == filter_words:
            new_vacancy = Vacancy(vacancy['name'], vacancy['url'], vacancy['salary'],
                                    vacancy['requirements'],vacancy['employer'], vacancy['description'])
            new_list.append(new_vacancy)
            JSONSaver.add_vacancy('filtered.json', new_vacancy)

    with open(superjob_vacancies, 'r', encoding='utf-8') as f:
        content = json.load(f)

    # Цикл по вакансиям superjob
    for vacancy in content:
        requirements = vacancy['requirements']
        if requirements is None:
            requirements = set()
        else:
            for s in requirements:
                if s in punc:
                    new_str = requirements.replace(s, "")
            requirements = set(new_str.lower().split())

        description = vacancy['description']
        if description is None:
            description = set()
        else:
            for s in description:
                if s in punc:
                    new_str = description.replace(s, "")
            description = set(new_str.lower().split())

        if filter_words.intersection(requirements.union(description)) == filter_words:
            new_vacancy = Vacancy(vacancy['name'], vacancy['url'], vacancy['salary'],
                                  vacancy['requirements'], vacancy['employer'], vacancy['description'])
            new_list.append(new_vacancy)
            JSONSaver.add_vacancy('filtered.json', new_vacancy)

    return new_list


def sort_by_salary(vacancy):
    """Функция ключа сортировки"""
    if vacancy.salary:
        if vacancy.salary['from']:
            return vacancy.salary['from']
    return 0


def sort_vacancies(filtered_vacancies):
    """Функция, сортирующая вакансии по зарплате от большей к меньшей"""
    filtered_vacancies.sort(key=sort_by_salary, reverse=True)
    return filtered_vacancies


def get_top_vacancies(sorted_vacancies, top_n):
    """Функция, возвращающая N первых вакансий"""
    return sorted_vacancies[:top_n]


def print_vacancies(vacancies):
    """Функция печати списка вакансий"""
    for i in range(len(vacancies)):
        print(i+1)
        print(vacancies[i])
