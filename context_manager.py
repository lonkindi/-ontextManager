import datetime


class MyContextManager:
    runtime = 0

    def __init__(self, file_path):
        self.file_path = file_path
        print('*' * 15, 'Блок информации менеджера контекста', '*' * 15)
        print(f'Время инициализации менеджера контента: {datetime.datetime.now()}')
        self.runtime = datetime.datetime.now()

    def __enter__(self):
        self.file = open(self.file_path, encoding='utf-8')
        print(f'Время открытия файла: {datetime.datetime.now()}')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Ошибки выполнения кода:\nexc_type = {exc_type}\nexc_val = {exc_val}\nexc_tb = {exc_tb}')
        self.file.close()
        print(f'Время закрытия файла: {datetime.datetime.now()}')
        print(f'Потрачено времени на выполнение кода: {datetime.datetime.now() - self.runtime}')
        print('*' * 22, 'Конец блока информации', '*' * 22, '\n')
