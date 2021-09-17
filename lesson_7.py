a, b, c = [
    float(x) for x in input('Введите длины отрезков, через пробел: ').split()
]
# Необходимым и достаточным условием существования треугольника является
# выполнение следующих неравенств: a<b+c, b<a+c, c<a+b, (a>0, b>0, c>0)
if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print(f'Треугольник со сторонами {a} {b} {c} - равносторонний')
    elif a == b or b == c or c == a:
        print(f'Треугольник со сторонами {a} {b} {c} - равнобедренный')
    else:
        print(f'Треугольник со сторонами {a} {b} {c} - разносторонний')
else:
    print(f'Треугольника со сторонами {a} {b} {c} не существует')
