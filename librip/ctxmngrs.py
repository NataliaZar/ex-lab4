# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
#with timer():
#  sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5

from datetime import datetime


class timer():
    def __enter__(self):
        self.now = datetime.now()

    def __exit__(self, exp_type, exp_value, traceback):
        print(datetime.now() - self.now)