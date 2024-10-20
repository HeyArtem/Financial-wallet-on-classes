class classproperty(object):
    """
        Рукописный декоратор. Использую его в class Transaction.list_transactions
        в геттере
    """
    def __init__(self, function):
        self.function = function

    def __get__(self, instance, owner):
        return self.function(owner)