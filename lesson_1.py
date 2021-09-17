numb = input('Введите число: ')

sum = 0
prod = 1

for i in numb:
    sum += int(i)
    prod *= int(i)
print(f"Сумма цифр числа {numb}: {sum}")
print(f"Произведение цифр: {numb}: {prod}")
