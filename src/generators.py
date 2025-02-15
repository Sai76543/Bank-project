


def filter_by_currency(transactions: list[dict], currency: str = "USD"):
    """Принимает список словарей, представляющих транзакции. Возвращает по одному словарю из списка, в котором валюта
        операции соответствует заданной валюте"""
    for transact in transactions:
        if transact["operationAmount"]["currency"]["code"] == currency:
            yield transact


def transaction_descriptions(transactions: list[dict]):
    """Принимает список словарей, представляющих транзакции. Возвращает описания каждой операции из списка по одному"""
    for transact in transactions:
        yield transact["description"]


def card_number_generator(start: int, stop: int):
    """Генератор номера банковских карт в заданом диапозоне от начального значения(start)
    до конечного(end) включительно"""
    for card_number in range(start, stop + 1):
        str_card_number = str(card_number).zfill(16)
        formatted_number = ' '.join([str_card_number[i:i + 4] for i in range(0, 16, 4)])
        yield formatted_number

for card_number in card_number_generator(1, 5):
    print(card_number)






