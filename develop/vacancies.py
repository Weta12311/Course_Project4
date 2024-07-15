class Vacancy:
    """Класс для работы с вакансиями"""
    def __init__(self, name: str, salary, url: str, employer: str):
        self.name = name
        self.url = url
        self.employer = employer
        self.validate_salary(salary)

    def validate_salary(self, salary):
        if salary is None:
            self.salary_from = 0
            self.salary_to = 0
        else:
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else 0
            '''перевод иностранной валюты в рубли'''
            if salary["currency"] == "USD":
                self.salary_from = self.salary_from * 100
                self.salary_to = self.salary_to * 100
            if salary["currency"] == "UZS":
                self.salary_from = int(self.salary_from * 0.007)
                self.salary_to = int(self.salary_to * 0.007)
            if salary["currency"] == "BYR":
                self.salary_from = int(self.salary_from * 27)
                self.salary_to = int(self.salary_to * 27)
            if salary["currency"] == "KZT":
                self.salary_from = int(self.salary_from * 0.2)
                self.salary_to = int(self.salary_to * 0.2)


    def __str__(self):
        return f"""Профессия: {self.name}
Зарплата от {self.salary_from} руб. до {self.salary_to} руб.
url: {self.url}
Название компании: {self.employer}"""