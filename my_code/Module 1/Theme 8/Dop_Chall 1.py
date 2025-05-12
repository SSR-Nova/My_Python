<<<<<<< HEAD
while True:
    book = input('Введите книгу и автора(формат: название, автор): ').strip()
    if ',' not in book:
        print('Ошибка: используйте формат: название, автор')
        continue
    save_book = [item.strip() for item in book.split(',', 1)]

    if not all(save_book):
        print('Ошибка: введите название и автора')
        continue


    with open('library.txt', 'a', encoding='utf-8') as file:
        file.write(f'Название: {save_book[0]} | Автор: {save_book[1]}\n')
        print(f'Данные сохранены!')
        break

=======
while True:
    book = input('Введите книгу и автора(формат: название, автор): ').strip()
    if ',' not in book:
        print('Ошибка: используйте формат: название, автор')
        continue
    save_book = [item.strip() for item in book.split(',', 1)]

    if not all(save_book):
        print('Ошибка: введите название и автора')
        continue


    with open('library.txt', 'a', encoding='utf-8') as file:
        file.write(f'Название: {save_book[0]} | Автор: {save_book[1]}\n')
        print(f'Данные сохранены!')
        break

>>>>>>> d6adf397ce76f5063ab9da53365e45c33c9cf186
