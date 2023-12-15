import json


class JSONSaver():
    def save_to_json(data):
        with open(filename, 'a') as f:
            json.dump(data, f)


    def add_vacancy(self, vacancy):
        pass

    def delete_vacancy(self, vacancy):
        pass


    def get_vacancies_by_salary(self, salary: str):
        pass
