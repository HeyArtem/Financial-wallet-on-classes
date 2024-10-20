from models.transaction import Transaction
from models.stream import Stream
"""
    Инициализация
"""
# str1 = Stream()
# print(str1.read())


"""
    Записать транзакцию, что бы присваивался pk:
    -Прочитал тра-ции в  __LIST_TRANSACTIONS:
        [созд экз кл Stream, вызвал Transaction.append 
        & скормил ему экз кл Stream с методом read ]   
    -Coзд экз кл Transaction
    -Вызвал экз кл Stream.write (cкормил ему экз кл Transaction)         
"""

# str1= Stream()
# Transaction.append(str1.read())
#
# tr1 = Transaction(
#     category='расход',
#     date='2000-01-20',
#     amount=1500,
#     description=" test date"
# )
# str1.write(tr1)
# print(tr1.date,)

"""
test list_transactions:
(Возвощает список транзакций в виде экземпляров кл.)
    создал экз класса Stream
    Обратился к кл Transaction-> m append-> 
        передал ему эк.кл Stream+m read(читает из файла)
"""
# str_r = Stream()
# Transaction.append(str_r.read())
# print(Transaction.list_transactions)

"""
    test show_income (доходы)
"""
# str1 = Stream()
# Transaction.append(str1.read())
# print(Transaction.show_income())


"""
    test show_expense (расходы)
"""
# str1 = Stream()
# Transaction.append(str1.read())
# print(Transaction.show_expense())

"""
    test show_balance (баланс)
"""
# str1 = Stream()
# Transaction.append(str1.read())
# print(Transaction.show_balance())


"""
    test search_id
"""
# str1 = Stream()
# Transaction.append(str1.read())
# print(Transaction.search_id(12))

"""
    test search_category
"""
# str1 = Stream()
# Transaction.append(str1.read())
# print(Transaction.search_category('расход '))


"""
    test search
"""
str1 = Stream()
Transaction.append(str1.read())
print(Transaction.search(
    field='amount',
    keyword=100
    # keyword='2024-10-12'
    # keyword='100'
))

# """
#     search by category
# """
# str1 = Stream()
# Transaction.append(str1.read())
# result_category = Transaction.search_by_category('Расход ')
# print(result_category)


"""
    search by sum
"""
# str1 = Stream()
# Transaction.append(str1.read())
# result_sum = Transaction.search_by_sum(60)
# print(result_sum)

"""
    test date_generation
"""
# str1 = Stream()
# print(str1.date_generation())

"""
    test read
"""
# str1 = Stream()
# res = str1.read()
# for transaction in res:
#     print(transaction, type(transaction['pk']))
#     print(type(transaction['date']))
#     print(type(transaction['amount']))




















