# задание 1: Работа с типами данных
a = "Привет"
b = 42
c = 3.14
d = [ 1, 2, 3 ]

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# задание 2: Преобразование регистра строк
text = "python PROGRAMMING"
print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.title())

# задание 3: Удаление пробелов
hello = "  Hello World  "
print(hello.strip())
print(hello.lstrip())
print(hello.rstrip())

# задание 4: Разделение и объединение строк
my_text = "яблоко,банан,апельсин,груша"
my_list = (my_text.split(","))
print(" | ".join(my_list))

# задание 5: Замена подстрок
learn = "Я изучаю Python. Python - это круто!"
new_learn = learn.replace("Python", "Java")
print(new_learn)

# задание 6: Поиск и подсчет
text_1 = "Python программирование на Python"
print(text_1.find("Python"))
print(text_1.count("Python"))
print(text_1.find("Java"))

# задание 7: Проверка типа символов
print("Hello123".isalnum())
print("12345".isdigit())
print("Hello".isalpha())
print("   ".isspace())

# задание 8: Срезы строк
text_2 = "Python very good"
print(text_2[:3])
print(text_2[-3:])
print(text_2[1::2])
print(text_2[::-1])

# задание 9 : Экранирование символов
text_3 = "Он сказал: \"Привет\""
print(text_3)
text_4 = "Первая строка \nВторая строка"
print(text_4)
