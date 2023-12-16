from abc import ABC, abstractmethod
from src.vacancy import Vacancy
import json


class FileProcessor(ABC):

    @abstractmethod
    def save_to_json(self):
        pass

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self):
        pass


class JSONSaver(FileProcessor):

    def __init__(self):
        pass

    def save_to_json(self, filename, data):
        for vacancy in data['items']:
            name = vacancy['name']
            url = vacancy['url']
            salary = vacancy['salary']
            requirements = vacancy['snippet']['requirement']
            employer = vacancy['employer']['name']
            description = vacancy['snippet']['responsibility']
            new_vacancy = Vacancy(name, url, salary, requirements, employer, description)
            self.add_vacancy('vacancies.json', new_vacancy)
            print(new_vacancy)

    @staticmethod
    def add_vacancy(filename, vacancy):
        with open(filename, 'a', encoding='utf-8') as f:
            json.dump(vacancy.__dict__(), f)

    @staticmethod
    def delete_vacancy(filename, vacancy):
        with open(filename, 'r', encoding='utf-8') as f:
            new_dict = json.load(f)
        for item in new_dict['items'][0]:
            if item['name'] == vacancy.name:

                del new_dict['items'][0]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    @staticmethod
    def get_vacancies_by_salary(salary: str):
        pass
