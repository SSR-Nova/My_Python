def analiz_text(filename, filename_2):

    # Создаю список символов, которые нужно убрать из текста
    znaki = ['.', ',', '!', '?', '-', '+']

    # Открываю файл
    with open(filename, 'r') as file:
        # Читаем файл
        text = file.read()

        # Перебираем знаки которые необходимо убрать
        for old_znak in znaki:
            # заменяем эти знаки
            text = text.replace(old_znak, '')

        # Приводим весь текст к нижнему регистру    
        text = text.lower()

        # Разделяем каждый элемент текста
        text = text.split()

        # Создаем переменную для подсчёта количества слов в тексте
        all_count_word = len(text)

        # Создаем пустой словарь для подсчёта кол-ва каждого слова
        count_word = {}

        # Перебираем все слова из текста
        for word in text:
            # Если слова нет в словаре, то добавляем (слово - ключ) и придаем значение 1
            if word not in count_word:
                count_word[word] = 1
            # Если слово уже есть, увеличиваем его значение в словаре на 1    
            else:
                count_word[word] += 1
        
        # Создаем переменную для хранения слова
        word = ''
        # Создаем переменную для хранения количества использований слова в тексте
        symbol_word = 0

        # Перебираем слова по ключ,значение
        for key, value in count_word.items():
            # Если значение больше переменной symbol_word
            if value > symbol_word:
                # Заменяем значение
                symbol_word = value
                # Заменяем слово
                word = key

    # Записываем в другой файл результаты анализа текста из первого файла    
    with open(filename_2, 'w') as file:
        file.write(f'Количество слов в тексте: {all_count_word}\n')
        file.write(f'Каждое слово и его количество в тексте:\n')
        for key, value in count_word.items():
            file.write(f'{key} : {value}\n')
        file.write(f'Самое часто используемое слово: {word}, количество использования в тексте: {symbol_word}\n')
        

    


analiz_text('1.txt', '2.txt')