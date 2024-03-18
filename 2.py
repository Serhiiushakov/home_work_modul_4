from pathlib import Path

def get_cats_info(path):
    cat_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:
                    cat_info = {
                        "id": cat_data[0].strip(),
                        "name": cat_data[1].strip(),
                        "age": cat_data[2].strip()
                    }
                    cat_list.append(cat_info)
                else:
                    print(f"Неправельний формат: {line}")
        return cat_list
    except FileNotFoundError:
        print("файл не знайдено")
    except Exception as e:
        print(f"сталася помилка: {e}")
        return []


path = 'dz/cats_f.txt'  # текстовий файл cats_f.txt знаходиться в папці dz
                      
   
cats = get_cats_info(path)
for cat in cats:
    print(cat)

