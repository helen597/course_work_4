from abc import ABC, abstractmethod


class VacanciesAPI(ABC):

    @abstractmethod
    def get_vacancies(self, name):
        pass


class HeadHunterAPI(VacanciesAPI):
    def get_vacancies(self, name):
        pass


class SuperJobAPI(VacanciesAPI):
    def get_vacancies(self, name):
        pass
