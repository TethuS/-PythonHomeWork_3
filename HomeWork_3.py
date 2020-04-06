some_text = open('text.txt', 'r', encoding='UTF-8')
some_text = some_text.read()

# Задание 1. Очистка от знаков препинания
punct_marks = [',', '.', '!', '?', '«', '»', '—', ';','(',')']  # Список со знаками препинания

for mark in punct_marks:  # Проходимся циклом по каждому символу из Списка
    if mark in some_text:  # Проверяем есть ли этот символ в тексте
        some_text = some_text.replace(mark, '')  # Убираем обнаруженный символ
print(some_text)

# Задание 2. Сформировать list со словами (split)
text_list = list(some_text.split()) # Разбиваем текст по словам на отдельный элемент Списка
print(text_list)

# Задание 3. Привести все слова к нижнему регистру (map)
new_text_list = list(map(lambda x: x.lower(), text_list)) # Поэлементно приводим каждое слово к нижнему регистру
print(new_text_list)

# Заданиче 4. Получить из list п.3 dict, ключами - слова, а значениями - количество появлений в тексте;
words_count = {}
for i in range(len(new_text_list)): # Проходимся по Списку с нижним регистром
    # Создаем Ключ соответсвующий слову из Списка, а методом .count(), записываем кол-во элементов в Значение
    words_count[new_text_list[i]] = new_text_list.count(new_text_list[i])
print(words_count)

# Задание 5. Вывести 5 наиболее часто встречающихся слов (sort) и количество разных слов в тексте (set).
words_count_list=list(words_count.items()) # Преобразуем Словарь в Список
# Сортируем элементы по кол-ву повторений (повторения идут под индексом 1) и указываем обратный порядок
top_words=words_count_list.sort(key=lambda x: x[1], reverse=True)

print(words_count_list[:5]) # Срезом выводим первые 5 элементов