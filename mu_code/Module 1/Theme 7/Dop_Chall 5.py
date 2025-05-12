date = input('Введите дату в формате ДД.ММ.ГГГГ: ')

try:
    day, month, year = date.split('.')
    
    # Проверяем, что все части состоят из цифр и имеют нужную длину
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        raise ValueError("Дата должна содержать только цифры")
    
    day = int(day)
    month = int(month)
    year = int(year)

    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        raise ValueError("День и месяц должны быть из 2 цифр, год — из 4")

    if month < 1 or month > 12:
        raise ValueError("Месяц должен быть от 1 до 12")

    if day < 1 or day > 31:
        raise ValueError("День должен быть от 1 до 31")

    # Проверка для месяцев с 30 днями
    if month in [4, 6, 9, 11] and day > 30:
        raise ValueError(f"В {month} месяце не может быть больше 30 дней")

    # Проверка для февраля (без учёта високосных лет)
    if month == 2 and day > 28:
        raise ValueError("В феврале не может быть больше 28 дней")

    print("Дата корректна:", f"{day:02d}.{month:02d}.{year}")

except ValueError as e:
    print("Ошибка:", e)