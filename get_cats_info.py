def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                cat = {
                    "id": data[0],
                    "name": data[1],
                    "age": data[2]
                }
                cats.append(cat)
        return cats
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
    except IndexError:
        print("Помилка формату даних у файлі.")
        return []
    
cats_info = get_cats_info("task2\cats_file.txt")
print(cats_info)
