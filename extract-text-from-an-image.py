
import pytesseract
from PIL import Image

# Открываем изображение
img = Image.open('im.png')

# Извлекаем текст с помощью pytesseract
text = pytesseract.image_to_string(img, lang='rus')

# Записываем текст в файл
with open('file.txt', mode='w', encoding='utf-8') as file:
    file.write(text)


# В этом примере image.png - это имя файла изображения, 
# которое нужно заменить на имя своего файла, а file.txt - это имя файла, 
# в который будет записан извлеченный текст. Если изображение содержит текст на русском языке, 
# то для корректного распознавания нужно указать язык с помощью параметра lang='rus'. 
# Если язык не указан, pytesseract будет использовать английский язык распознавания по умолчанию.
