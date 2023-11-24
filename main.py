import re


def read_and_process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            first_sentence = file.readline().strip()
            print("Перше речення:", first_sentence)
            text = file.read()

            words = re.findall(r'\b\w+\b', text.lower())
            ukrainian_words = sorted([word for word in words if re.match('[а-яіїєґ]+', word)])
            english_words = sorted([word for word in words if re.match('[a-z]+', word)])

            print("\nУкраїнські слова:")
            print("\n".join(ukrainian_words))
            print("Кількість українських слів:", len(ukrainian_words))

            print("\nАнглійські слова:")
            print("\n".join(english_words))
            print("Кількість англійських слів:", len(english_words))

    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

file_path = 'text.txt'
read_and_process_file(file_path)
