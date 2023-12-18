from abc import ABC, abstractmethod
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
                json.dump([vacancy.__dict__()], f, ensure_ascii=False)
        else:
            with open(filename, 'r', encoding='utf-8') as f:
                content = json.load(f)
                content.append(vacancy.__dict__())
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(content, f, ensure_ascii=False)

    @staticmethod
    def delete_vacancy(filename, vacancy_name):
        with open(filename, 'r', encoding='utf-8') as f:
            content = json.load(f)
        for i in range(len(content)):
            print(content[i])
            if content[i]['name'] == vacancy_name:
                del content[i]
                break
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False)

    def get_vacancies_by_salary(self):
        pass
