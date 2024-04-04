# Моя программа v 1

print("Привет! Предлагаю проверить свои знания английского !")

print("Расскажи, как тебя зовут ! ")
name = input("")
max_bal = 30
question = 0
proc = 100

print(f" Привет,{name}, начинаем тренировку! ")

print("Вопрос:My name __ Vova")
one = str(input("Ответ "))
if one == "is":
    print("Ответ верный!")
    print("Вы получаете 10 балов!")
    question += 1
else:
    max_bal -= 10
    proc -= 33
    print("Неправильно.")
    print("Правильный ответ: is")

print("Вопрос: I __ a coder")
two = str(input("Ответ "))
if two == "am":
    question += 1
    print("Ответ верный!")
    print("Вы получаете 10 балов!")
else:
    max_bal -= 10
    proc -= 33
    print("Неправильно.")
    print("Правильный ответ: am")


print("Вопрос: I live __ Moscow")
free = str(input("Ответ "))
if free == "in":
    question += 1
    print("Ответ верный!")
    print("Вы получаете 10 балов!")
else:
    max_bal -= 10
    proc -= 33
    print("Неправильно.")
    print("Правильный ответ: in")

print(f"Вот и все, {name}")
print(f"Вы ответили на {question} из 3 вопросов")
print(f"Вы заработали {max_bal} из 30")
print(f"это {proc} процентов ")

# пРОВЕРКА