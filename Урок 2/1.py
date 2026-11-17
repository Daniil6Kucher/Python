surname = input("Введіть прізвище студента: ")
score = int(input("Введіть кількість балів: "))

if score > 80:
  print(f"Студент {surname} здав іспит.")
else:
  print(f"Студент {surname} іспит не складено.")