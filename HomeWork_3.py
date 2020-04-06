some_text = open('text.txt', 'r', encoding='UTF-8')
some_text = some_text.read()

# Задание 1. Очистка от знаков препинания
punct_marks = [',', '.', '!', '?', '«', '»', '—', ';']  # Список со знаками препинания

for mark in punct_marks:  # Проходимся циклом по каждому символу из списка
    if mark in some_text:  # Проверяем есть ли этот символ в тексте
        some_text = some_text.replace(mark, '')  # Убираем обнаруженный символ
print(some_text)

# Задание 2. Сформировать list со словами (split)
text_list = list(some_text.split())
print(text_list)

# Задание 3. Привести все слова к нижнему регистру (map)
new_text_list = list(map(lambda x: x.lower(), text_list))
print(new_text_list)