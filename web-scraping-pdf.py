# Скрапинг сайта и извлечение из него все файлы в формате pdf

import requests
import os
from bs4 import BeautifulSoup
# адрес сайта с которого нужно сказать файлы pdf, важно вставить ulr на котором есть линки на pdf файлы
url = 'https://gigacloud.ua/services/instrukcii'

# Создаем директорию, если ее нет, сюда буду скачаны файлы pdf
if not os.path.exists('directory-downloadpdf'):
    os.makedirs('gigacloud-ua-pdf')

# Получаем содержимое страницы
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Ищем ссылки на pdf-файлы
pdf_links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None and href.endswith('.pdf'):
        pdf_links.append(href)

# Скачиваем pdf-файлы
for pdf_link in pdf_links:
    pdf_response = requests.get(pdf_link)
    file_name = pdf_link.split('/')[-1]
    file_path = os.path.join('gigacloud-ua-pdf', file_name)
    with open(file_path, 'wb') as f:
        f.write(pdf_response.content)

# В этом примере мы создаем директорию gigacloud-ua-pdf, если она еще не существует, 
# используя метод os.makedirs(). Затем мы создаем переменную file_path, 
# которая содержит относительный путь к файлу в директории gigacloud-ua-pdf. 
# Мы используем метод os.path.join(), чтобы объединить имя файла и путь к директории в одну строку. 
# Затем мы сохраняем содержимое файла PDF в указанную директорию и файл с помощью метода open().
