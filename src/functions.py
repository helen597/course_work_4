import json


def filter_vacancies(hh_vacancies, superjob_vacancies, filter_words):
    new_list = []
    with open(hh_vacancies, 'r', encoding='utf-8') as f:
        content = json.load(f)
    for vacancy in content:
        if filter_words in vacancy['requirements'] or filter_words in vacancy['description']:
            new_list.append(vacancy.__dict__())
    with open(superjob_vacancies, 'r', encoding='utf-8') as f:
        content = json.load(f)
    for vacancy in content:
        if filter_words in vacancy['requirements'] or filter_words in vacancy['description']:
            new_list.append(vacancy.__dict__())
    return new_list


def sort_vacancies(filtered_vacancies):
    with open(filtered_vacancies, 'r', encoding='utf-8') as f:
        content = json.load(f)
        for vacancy in content:
            if vacancy['salary'] is None:
                vacancy['salary']['from'] = 0
            else:
                if vacancy['salary']['from'] is None:
                    vacancy['salary']['from'] = 0
        new_list = sorted(content, key=['salary']['from'], reverse=True)
        return new_list


def get_top_vacancies(sorted_vacancies, top_n):
    return sorted_vacancies[:top_n]


def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy)
