import json


def filter_vacancies(hh_vacancies, superjob_vacancies, filter_words):
    new_list = []

    with open(hh_vacancies, 'r', encoding='utf-8') as f:
        content = json.load(f)

    filter_words = set(filter_words)

    punc = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

    for vacancy in content:
        # vacancy = Vacancy(vacancy)
        print(vacancy)
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
            new_list.append(vacancy)
    # with open(superjob_vacancies, 'r', encoding='utf-8') as f:
    #     content = json.load(f)
    # for vacancy in content:
    #     try:
    #         requirements = set(vacancy['requirements'].replace('.', ' ').lower().split())
    #         print(vacancy['requirements'])
    #         print(requirements)
    #         description = set(vacancy['description'].replace('.', ' ').lower().split())
    #         print(vacancy['description'])
    #         print(description)
    #     except AttributeError:
    #         print('ошибка атрибута')
    #     for i in range(len(filter_words)):
    #         if filter_words.intersection(requirements) or filter_words.intersection(description):
    #             new_list.append(vacancy.__dict__())
    with open('filtered.json', 'w', encoding='utf-8') as f:
        json.dump(new_list, f, ensure_ascii=False)
    return new_list


def sort_vacancies(filtered_vacancies):

    # for vacancy in filtered_vacancies:
    #     if vacancy['salary'] is None:
    #         vacancy['salary']['from'] = 0
    #     else:
    #         if vacancy['salary']['from'] is None:
    #             vacancy['salary']['from'] = 0
    # new_list = sorted(content, key=['salary']['from'], reverse=True)
    print('Отсортированные:')

    for i in range(len(filtered_vacancies)):
        print(filtered_vacancies[i])
    return filtered_vacancies
    # return new_list


def get_top_vacancies(sorted_vacancies, top_n):
    return sorted_vacancies[:top_n]


def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy)
