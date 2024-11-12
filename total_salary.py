def total_salary(path):
    try:
        with open("salary_file.txt", 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                # Видаляємо зайві пробіли та розділяємо рядок за комою
                data = line.strip().split(',')
                # Перетворюємо зарплату на число та додаємо до списку
                salary = int(data[1])
                salaries.append(salary)
            
            # Обчислюємо загальну та середню зарплати
            total = sum(salaries)
            average = total / len(salaries) if salaries else 0  # Перевірка, щоб уникнути ділення на нуль

            return total, average

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None
    except ValueError:
        print("Неправильний формат даних у файлі.")
        return None
    except TypeError:
        print("Cannot unpack non-iterable Nonetype object")
        return None

total, average = total_salary("task1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

