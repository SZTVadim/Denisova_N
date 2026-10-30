# ЗАДАНИЕ 1: Работа со словарями и перебор элементов
student = {
    "name": "Иван",
    "age": 20,
    "year_study": 2,
    "city": "Москва"
}
print(student.keys())
print(student.values())
for key, value in student.items():
    print(key, value)
for value in student.values():
    print(value)

# ЗАДАНИЕ 2: Удаление элементов и генератор словарей

prices = {
    "яблоко": 50,
    "банан": 30,
    "апельсин": 40,
    "груша": 35,
    "виноград": 60
}
del prices["груша"]
remove_v = prices.pop("виноград")
new_prices = {x: y*0.9 for x, y in prices.items()}
print(new_prices)

# ЗАДАНИЕ 3: Объединение словарей

student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}
student3 = {**student1, **student2}
student1.update(student2)
print(student1)
print(student2)
print(student3)
