some_text = open('text.txt', 'r', encoding='UTF-8')
some_text = some_text.read()

# Задание 1. Очистка от знаков препинания
punct_marks = [',', '.', '!', '?', '«', '»', '—', ';','(',')']  # Список со знаками препинания

for mark in punct_marks:  # Проходимся циклом по каждому символу из списка
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
for i in range(len(new_text_list)): # Проходимся по списку с нижним регистром
    # Создаем ключ соответсвующий слову из списка, а методом .count(), записываем кол-во элементов
    words_count[new_text_list[i]] = new_text_list.count(new_text_list[i])
print(words_count)



