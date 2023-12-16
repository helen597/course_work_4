from abc import ABC, abstractmethod
import requests


class VacanciesAPI(ABC):

    @abstractmethod
    def get_vacancies(self, name):
        pass


class HeadHunterAPI(VacanciesAPI):
    url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, name):
        response = requests.get(self.url, params={"text": name})
        response.raise_for_status()
        print(response.json())
        # vacancies = {vacancy for vacancy in response.json().get(['items'][0])}
        # skills = [skill['name'] for skill in data.get('key_skills', [])]
        # return ', '.join(skills)
        # print(vacancies)
        return response.json()


class SuperJobAPI(VacanciesAPI):
    url = "https://api.superjob.ru/"
    api_key = "v3.r.117049901.e9497899abcec38b14ed280a08038391982a2d1b.b20a5069ace9a4b84655ff985b7bb2a848db94f2"

    def get_vacancies(self, name):
        response = requests.get(self.url, headers={"X-Api-App-Id": self.api_key})
