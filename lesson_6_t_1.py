#  Windows 10, версии: 20H2
#  Python 3.9.2


import sys


def memory_count(lst):
    memory = 0

    for var in lst:
        print('***********')
        print(f'Переменная: {var}')
        print('Весит: ', sys.getsizeof(var))
        spam = sys.getsizeof(var)

        if hasattr(var, '__iter__') and not isinstance(var, str):

            if hasattr(var, 'keys'):
                for key, value in var.items():
                    print(f'\nКлюч: \'{key}\' значение {value}')
                    spam += memory_count([key]) + memory_count([value])

            else:
                spam += memory_count(var)

        memory += spam

    return memory


# Проверим работу:
# Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.

numb = input('Введите число: ')

sum = 0
prod = 1

for i in numb:
    sum += int(i)
    prod *= int(i)
print(f"Сумма цифр числа {numb}: {sum}")
print(f"Произведение цифр: {numb}: {prod}")

_variable = []
for i in dir():
    if i[0] != '_' and not hasattr(locals()[i], '__name__'):
        _variable.append(locals()[i])

print('\nПеременные: ', _variable, '\n')
print('\nЗатраты памяти программы: ', memory_count(_variable))

# Затраты памяти программы: 158
