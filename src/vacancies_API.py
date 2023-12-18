import json
from abc import ABC, abstractmethod
import requests
from src.JSON_processor import JSONSaver
from src.vacancy import Vacancy


class VacanciesAPI(ABC):

    @abstractmethod
    def get_vacancies(self, name):
        pass

    @abstractmethod
    def save_to_json(self):
        pass


class HeadHunterAPI(VacanciesAPI):
    url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, name):
        response = requests.get(self.url, params={"text": name})
        return response.json()

    def save_to_json(self, filename, data):
        for vacancy in data['items']:
            name = vacancy['name']
            url = vacancy['alternate_url']
            salary = vacancy['salary']
            requirements = vacancy['snippet']['requirement']
            employer = vacancy['employer']['name']
            description = vacancy['snippet']['responsibility']
            new_vacancy = Vacancy(name, url, salary, requirements, employer, description)
            JSONSaver.add_vacancy('hh_vacancies.json', new_vacancy)


class SuperJobAPI(VacanciesAPI):
    url = "https://api.superjob.ru/2.0/vacancies/"
    api_key = "v3.r.117049901.e9497899abcec38b14ed280a08038391982a2d1b.b20a5069ace9a4b84655ff985b7bb2a848db94f2"

    def get_vacancies(self, name):
        response = requests.get(self.url, headers={"X-Api-App-Id": self.api_key},
                                params={"keyword": name})
        # print(print(response.json()))
        return response.json()

    def save_to_json(self, filename, data):
        for vacancy in data['objects']:
            name = vacancy['profession']
            url = vacancy['link']
            salary = {'from': vacancy['payment_from'],
                      'to': vacancy['payment_to'],
                      'currency': vacancy['currency'],
                      'gross': False}
            requirements = vacancy['candidat']
            employer = vacancy['firm_name']
            description = vacancy['work']
            new_vacancy = Vacancy(name, url, salary, requirements, employer, description)
            JSONSaver.add_vacancy('sj_vacancies.json', new_vacancy)
