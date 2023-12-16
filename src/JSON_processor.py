from abc import ABC, abstractmethod
from src.vacancy import Vacancy
import json, os


class FileProcessor(ABC):

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

    @staticmethod
    def add_vacancy(filename, vacancy):
        if not os.path.exists(filename):
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump([vacancy.__dict__()], f)
        else:
            with open(filename, 'r', encoding='utf-8') as f:
                content = json.load(f)
                content.append(vacancy.__dict__())
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(content, f)

    @staticmethod
    def delete_vacancy(filename, vacancy):
        with open(filename, 'r', encoding='utf-8') as f:
            new_dict = json.load(f)
        for item in new_dict:
            if item['name'] == vacancy.name:

                del new_dict['items'][0]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    @staticmethod
    def get_vacancies_by_salary(salary: str):
        pass
