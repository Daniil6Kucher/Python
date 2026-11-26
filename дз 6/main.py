suma = 0

for i in range(1, 101):
    if i % 2 != 0:
        suma += i

print("Сумма неправильных чисел:", suma)



text = input("Введите рядок: ")

first = text[0]
count = text.count(first)

print("Количество вхождений первой буквы:", count)