# ЗАДАНИЕ 1: Добавление элементов в список
fruits = ["яблоко"]
fruits.append("банан")
fruits.extend(["апельсин", "груша"])
fruits.insert(1,"виноград")

# ЗАДАНИЕ 2: Удаление элементов из списка
fruits = ["яблоко", "банан", "апельсин", "банан"]
fruits.remove("банан")
last_elem = fruits.pop()

# ЗАДАНИЕ 3: Поиск элементов в списке
fruits = ["яблоко", "банан", "апельсин", "банан"]
print(fruits.index("банан"))
print(fruits.count("банан"))

# ЗАДАНИЕ 4: Сортировка и реверс списка
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
numbers.reverse()
print(numbers)

# ЗАДАНИЕ 5: генератор списков, min, max
cube = [x ** 3 for x in range(1, 9)]
print(min(cube))
print(max(cube))

# ЗАДАНИЕ 6:
list_2 = [5, 12, 8, 15, 3, 20, 7, 18, 9, 11]
list_3 = [x for x in list_2 if x > 10]
print(sum(list_3))

# ЗАДАНИЕ 7:
words = ["москва", "санкт-петербург", "казань"]
words_1 = [w.capitalize() for w in words]
print(words_1)
