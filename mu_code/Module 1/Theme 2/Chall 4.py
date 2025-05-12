price = int(input('Введите стоимость товара: '))
sale = int(input('Введите процент скидки (число от 0 до 100): '))
final_price = price - (price * sale / 100)
print(f'Цена со скидкой: {final_price} руб.')
    