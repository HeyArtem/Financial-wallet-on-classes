"""
    Валидация на int | float
"""
# amount = (input('Введите сумму транзакции: '))
# def is_digit(string):
#     if string.isdigit():
#        return True
#     else:
#         try:
#             float(string)
#             return True
#         except ValueError:
#             return False
# print(is_digit(amount))
def is_digit():
    while True:
        amount = (input('Введите сумму транзакции: '))
        try:
            float(amount) or int(amount)
            return 'Ok'
        except Exception:
            print('че за фигня? ВВоди опять')
            continue



print(is_digit())
