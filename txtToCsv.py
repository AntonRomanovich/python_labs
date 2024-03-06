import csv
import random

def convert_to_english(full_name):
    translit_dict = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'YO', 'Ж': 'ZH', 'З': 'Z', 'И': 'I',
        'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
        'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ъ': '', 'Ы': 'Y', 'Ь': '',
        'Э': 'E', 'Ю': 'YU', 'Я': 'YA',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya'
    }

    english_name = ''.join(translit_dict.get(char, char) for char in full_name)
    return english_name

input_file = 'students.txt'
output_file = 'students.csv'

with open(input_file, 'r', encoding='utf-8') as txt_file, open(output_file, 'w', newline='') as csv_file:
    reader = txt_file.readlines()
    writer = csv.writer(csv_file, delimiter=";")
    writer.writerow(
        ['username', 'password', 'firstname', 'lastname', 'email', 'city', 'maildisplay', 'course1', 'groupe']
    )

    for line in reader:
        full_name = line.strip()
        english_name = convert_to_english(full_name)

        en_name, en_last_name, en_second_name = english_name.split(maxsplit=2)

        username = en_name[0].lower() + en_last_name.lower() + "2024"
        name, last_name, second_name = full_name.split(maxsplit=2)
        password = random.randint(1000, 9999)
        email = username + "@fiztest.gsu.by"
        city = "Гомель"

        writer.writerow(
            [username, password, name, last_name, email, city, 0, "ОБиП_ПМС", "МС-32 (2023-2024)"]
        )

print('Конвертация завершена. Результат записан в файл', output_file)