import datetime
from models.stream import Stream
from models.transaction import Transaction
import re

stream = Stream()
Transaction.append(stream.read())




def show_balance():
    return f"Баланс кошелька: {Transaction.show_balance()}"


def show_income():
    return f"Сумма доходов: {Transaction.show_income()}"


def show_expense():
    return f"Сумма расходов: {Transaction.show_expense()}"


def new_transaction():
    print("[!] Создаем транзакцию")
    amount = None
    while amount is None:
        try:
            amount = float(input('Введите сумму: ').strip())
        except (ValueError, TypeError):
            print("Вы ввели не числовое значение!")

    print('Доступные категории:')
    for key, value in Transaction.categories.items():
        print(f"\t Выберите \"{key}\" если \"{value.title()}\"")
    select_category = input('Введите значение: ').strip()
    while select_category not in Transaction.categories:
        print("[!] Вы ввели не правильную категорию")
        select_category = input('Введите значение: ').strip()

    description = input('Введите описание: ').strip()
    # date = datetime.now().strftime("%Y-%m-%d")
    date = str(datetime.date.today())
    transaction = Transaction(
        date=date,
        category=Transaction.categories[select_category],
        amount=amount,
        description=description
    )
    stream.write(transaction)
    return transaction


def search():
    """
        Основное меню, раздел поиск.
        Уточнеят у пользователя по какому параметру {1:'date', 2:'amount', 3:'category'}
        в зависимости от выбора вызывает
        search_date, search_amount, search_category.
    """
    while True:
        print('Раздел поиск')
        # Формирую список с категориями.
        list_categories = Transaction.search_fields

        # Формирую словарь вида {1: 'date', 2: 'amount', 3: 'category'}
        categories_dict = {}
        # for index in range(len(list_categories)):
        #     categories_dict[index + 1] = list_categories[index]

        for index, item in enumerate(list_categories):
            categories_dict[index + 1] = item

            # И вывожу меню
            print(f"\t {index + 1}. {item.title()}")

        # Поиск по каждому полю-отдельная функция (new globals())
        glb = globals()
        action_menu_search = {
            '1': glb['search_date'],
            '2': glb['search_amount'],
            '3': glb['search_category'],
        }

        user_action_search = input('Выберите поле поиска: ')
        # Валидация
        if user_action_search not in action_menu_search.keys():
            print('Вы ввели не корректное число')
            continue
        return action_menu_search[user_action_search]()


def search_date():
    """
        Зта фун-я вызывается, фун-ей search,
        если выполняется поиск по дате (1.Date)
    """
    while True:
        print('Поиск дате.')
        date = input("Введите дату в формате: yyyy-mm-dd: ")

        # Валидация
        pattern = re.compile(r"[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])$")
        if not re.match(pattern, date):
            continue
        res = Transaction.search(
            field='date',
            keyword=datetime.date(*map(lambda x: int(x), date.split("-")))
        )
        if not res:
            return 'По данному запросу ни чего не найдено.'
        return res


def search_amount():
    """
        Зта фун-я вызывается, фун-ей search,
        если выполняется поиск по дате (2.Amount)
    """
    while True:
        print('Поиск по сумме транзакции.')
        amount = input("Введите сумму транзакции: ")
        # Валидация
        try:
            float(amount)
        except (ValueError, TypeError):
            print('Транзакции это число!')
            continue
        res = (Transaction.search(field='amount', keyword=int(amount)))
        if not res:
            return 'По данному запросу ни чего не найдено.'
        return res


def search_category():
    """
        Зта фун-я вызывается, фун-ей search,
        если выполняется поиск по 3.Category ['доход', 'расход']
    """
    print('Поиск по категории доход, расход.')
    while True:
        for k,v in Transaction.categories.items():
            print(f"\tВыберите {k} если {v}")
        category = (input("Введите '+' или '-': "))

        # Валидация категории
        if category not in Transaction.categories.keys():
            print("Нужно выбрать '+' или '-' ")
            continue
        res = (Transaction.search(field='category', keyword=Transaction.categories[category]))
        if not res:
            return 'По данному запросу ни чего не найдено.'
        return res



        # # Валидация
        # try:
        #     float(amount)
        # except Exception:
        #     print('Сумма это число!')
        #     continue
        # res = (Transaction.search(field='category', keyword=amount))
        # if not res:
        #     return 'По данному запросу ни чего не найдено.'
        # return res


def list_transactions():
    for transaction in Transaction.list_transactions:
        print(transaction)
        print('-' * 30)
    return ''


menu = [
    '1. Показать баланс',
    '2. Показать доходы',
    '3. Показать расходы',
    '4. Новая транзакция',
    '5. Поиск по транзакциям',
    '6. Показать все транзакции'
]
action_menu = {
    '1': show_balance,
    '2': show_income,
    '3': show_expense,
    '4': new_transaction,
    '5': search,
    '6': list_transactions,
}


def show_menu():
    print("\t -- Меню --")
    for action in menu:
        print(action)
    print(show_balance())


while True:
    show_menu()
    user_action = input(f'Выбери действие (1-{len(menu)}): ').strip()
    if user_action not in action_menu.keys():
        print('Вы ввели не корректное число')
        continue
    result = action_menu[user_action]()
    print(result)
