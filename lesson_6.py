abc_number = int(input('Введите номер буквы в алфавите: '))

# Генерируем список букв
abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print(abc_list)
if abc_number <= len(abc_list):
    print(f'Буква под номером {abc_number}: {abc_list[abc_number - 1]}')
# Реализуем ответ, если пользователь вводит число > кол-ва букв алфавита
else:
    print(
      f'Введено число, превышающее количество букв в алфавите, попробуйте снова. Букв: {len(abc_list)}'
    )