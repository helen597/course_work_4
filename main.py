from src.vacancies_API import HeadHunterAPI, SuperJobAPI
from src.vacancy import Vacancy
from src.JSON_processor import JSONSaver
from src.functions import sort_vacancies, filter_vacancies, get_top_vacancies, print_vacancies


def main():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    # Получение вакансий с разных платформ
    hh_vacancies = hh_api.get_vacancies("Python")
    superjob_vacancies = superjob_api.get_vacancies("Python")

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    hh_api.save_to_json("hh_vacancies.json", hh_vacancies)
    superjob_api.save_to_json("sj_vacancies.json", superjob_vacancies)


# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = ["HeadHunter", "SuperJob"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    main()
    # user_interaction()
