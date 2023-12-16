class Vacancy:
    def __init__(self, name, url, salary, requirements, employer, description=''):
        self.name = name
        self.employer = employer
        self.url = url
        self.salary = salary
        self.requirements = requirements
        self.description = description

    def __str__(self):
        return f'{self.name}\n{self.employer}\n{self.salary}\n{self.requirements}\n{self.description}\n{self.url}\n'

    def __dict__(self):
        return {'name': self.name,
                'url': self.url,
                'salary': self.salary,
                'requirements': self.requirements,
                'description': self.description}

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __eq__(self, other):
        return self.salary == other.salary
