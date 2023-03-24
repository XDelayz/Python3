import re

# скрипт открывает файл file.txt и заменяет старое слово over на Babay
with open('file.txt', 'r') as file:
    file_content = file.read()
    updated_content = re.sub(r'\bover\b', 'Babayk', file_content)

# скрипт записывает изменения в новый файл new_file.txt
with open('new_file.txt', 'w') as new_file:
    new_file.write(updated_content)
