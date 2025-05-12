import os

dir_name = 'test_dir'
new_name = 'data'

try:
    os.mkdir(dir_name)  # Создаём директорию
    print(f'Директория "{dir_name}" создана.')
except FileExistsError:
    print(f'Директория "{dir_name}" уже существует.')

try:
    os.rename(dir_name, new_name)  # Переименовываем
    print(f'Директория переименована в "{new_name}".')
except FileNotFoundError:
    print(f'Директория "{dir_name}" не найдена.')
except FileExistsError:
    print(f'Директория "{new_name}" уже существует.')