from src.vacancies_API import HeadHunterAPI, SuperJobAPI
from src.functions import filter_vacancies, sort_vacancies, get_top_vacancies, print_vacancies
from src.JSON_processor import JSONSaver

HH_VACANCIES_FILE = "hh_vacancies.json"
SUPERJOB_VACANCIES_FILE = "sj_vacancies.json"


def main():
    """Функция для взаимодействия с пользователем"""
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    # Получение вакансий с разных платформ
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = hh_api.get_vacancies(search_query)
    superjob_vacancies = superjob_api.get_vacancies(search_query)

    # Сохранение информации о вакансиях в файл
    hh_api.save_to_json(HH_VACANCIES_FILE, hh_vacancies)
    superjob_api.save_to_json(SUPERJOB_VACANCIES_FILE, superjob_vacancies)

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower().split()
    filtered_vacancies = filter_vacancies(HH_VACANCIES_FILE, SUPERJOB_VACANCIES_FILE, filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print("ТОП вакансий:")
    print_vacancies(top_vacancies)
    vacancy_to_delete = input("Введите название вакансии, которую будем удалять: ")
    JSONSaver.delete_vacancy('filtered.json', vacancy_to_delete)
    salary_from = int(input("Введите минимальную зарплату: "))
    vacancies_by_salary = JSONSaver.get_vacancies_by_salary(salary_from)
    print_vacancies(vacancies_by_salary)


if __name__ == "__main__":
    main()
