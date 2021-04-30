class Error(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        global user_val
        while True:
            try:
                try:
                    user_val = int(input('Введите числа: '))
                    ex = input(f'Успешный ввод данных, добавляем "{user_val}" в список. Чтобы продолжить нажмите '
                               f'"Enter": ').lower()
                    self.my_list.append(user_val)
                    if ex == 'n':
                        print(self.my_list)
                        break
                except ValueError:
                    raise Error
            except Error:
                ex = input(f'Вы ввели не число! Чтобы продолжить нажмите "Enter": ').lower()
                if ex == 'n':
                    print(self.my_list)
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()