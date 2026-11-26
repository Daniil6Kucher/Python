suma = sum(range(1, 101, 2))
print("Сума:", suma)

word = input("Введіть рядок: ")

count = 0

for letter in word:
    if letter == word[0]:
        count += 1

print("Кількість входжень:", count)

word = input("Введіть рядок:")
print("Введіть ваше запрошенння")
