class OrderTooBigError(Exception):
    pass
class InvalidPyamentMethodError(Exception):
    pass
class DeliveryUnavailableError(Exception):
    pass

def market(items, stock):
    for item, quantity in items.items():
        if quantity > stock.get(item, 0):
            raise OrderTooBigError (f'Не хватает товара {item}')
        
def pay(pay_edit):
    payvariation = ['Банковская карта', 'СБП', 'Наличный расчёт']
    if pay_edit not in payvariation:
        raise InvalidPyamentMethodError (f'Выберите другой способ оплаты')
    
def delivery(citi):
    citis = ['Москва', 'Саратов', 'Энгельс', 'Сывтывкар']
    if citi not in citis:
        raise DeliveryUnavailableError (f'Доставка в {citi} не осуществляется')