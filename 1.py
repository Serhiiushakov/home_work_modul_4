from pathlib import Path

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_salary = 0
            num_developers = 0
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        salary = int(parts[1])
                        total_salary += salary
                        num_developers += 1
                    except ValueError:
                        print(f"Попередження: Невірний формат числа у рядку '{line.strip()}'")
                else:
                    print(f"Попередження: Невірний формат рядка '{line.strip()}'")

            if num_developers > 0:
                average_salary = total_salary / num_developers
                return total_salary, average_salary
            else:
                print("Попередження: Файл не містить даних про зарплати розробників.")
                return 0, 0
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Помилка: {e}")
        return 0, 0

path = 'dz/file.txt'    # текстовий файл file.txt знаходиться в папці dz
total_salary_result = total_salary(path)

print("Загальна сума заробітної плати:", total_salary_result[0])
print("Середня заробітна плата:", total_salary_result[1])
