from typing import Union
from utils import classproperty
import datetime
import re


class Transaction:
    __LIST_TRANSACTIONS: list = []
    __DEFAULT_PK: int = 1
    __SEARCH_FIELDS: list = ['date', 'amount', 'category']
    __CATEGORIES = {
        '+': 'доход',
        '-': 'расход'
    }

    def __init__(
            self,
            category: str,
            amount: Union[int, float],
            description: str,
            date: str = None,
            pk: int = None
    ) -> None:
        self.__validation_date(date)
        self.__validation_category(category)
        self.__validation_amount(amount)
        self.__validation_description(description)
        self.category: str = category.lower()
        self.date: datetime.date = self.__date_generation(date)
        self.amount: float = float(amount)
        self.description: str = description
        self.__pk: int = self.__convert_pk(pk) or self.__get_new_pk()
        self.list_transactions.append(self)

    @classmethod
    def __validation_date(cls, date) -> None:
        pattern = re.compile(r"[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])$")
        if not re.match(pattern, date):
            raise ValueError('Дата должна быть в формате: yyyy-mm-dd')

    @classmethod
    def __validation_category(cls, category) -> None:
        if category.lower() not in cls.categories.values():
            raise ValueError(f'Категория должна быть: {" или ".join(cls.categories.values())}')

    @classmethod
    def __validation_amount(cls, amount) -> None:
        if not isinstance(amount, (float, int)):
            raise ValueError(f'Количество должно быть числом')

    @classmethod
    def __validation_description(cls, description) -> None:
        if not isinstance(description, str):
            raise ValueError(f'Описание должно быть строкой')

    @classmethod
    def __date_generation(cls, date: Union[str, None]) -> datetime:
        """
            Генерация даты в виде  экз кл date
        """
        if not date:
            return datetime.date.today()
        return datetime.date(*map(lambda x: int(x), date.split("-")))

    @staticmethod
    def __convert_pk(value) -> Union[int, None]:
        """
            Принимает значение, выводит число,
            если данные в число невозможно конвертировать-вернет None
            и сработает __get_new_pk
        """
        try:
            return int(value)
        except (ValueError, TypeError):
            return None

    @classmethod
    def __get_new_pk(cls) -> int:
        """
            Если в __LIST_TRANSACTIONS есть данные-присвоит новый PK,
            или PK = __DEFAULT_PK
        """
        if not cls.list_transactions:
            return cls.__DEFAULT_PK
        return cls.list_transactions[-1].__pk + 1

    @property
    def pk(self) -> int:
        return self.__pk

    @classmethod
    def append(cls, transactions: list) -> None:
        """
            Принимает список со словарями (его дает Stream.read)
            и записывает его в __LIST_TRANSACTIONS.
        """
        for i in transactions:
            # cls.__LIST_TRANSACTIONS.append(cls(**i))
            cls(**i)

    @classproperty
    def list_transactions(cls) -> list:
        """
           Возвощает список транзакций в виде экземпляров кл.
        """
        return cls.__LIST_TRANSACTIONS

    @classmethod
    def show_income(cls) -> int:
        """ Доходы. """
        return sum(
            map(
                lambda x: x.amount,
                filter(lambda i: i.category == "доход", cls.list_transactions)
            )
        )

    @classmethod
    def show_expense(cls) -> int:
        """ Расходы. """
        # Var1
        # expense = sum([int(i.amount) for i in cls.list_transactions if i.category == "Расход"])

        expense = 0
        for i in cls.list_transactions:
            if i.category == "расход":
                expense += i.amount
        return expense

    @classmethod
    def show_balance(cls) -> int:
        """ Баланс. """
        return cls.show_income() - cls.show_expense()

    @classproperty
    def search_fields(cls):
        return cls.__SEARCH_FIELDS

    @classmethod
    def search(cls, field: str, keyword) -> list:
        """ Поиск """
        print('[!] def search:', field, keyword)

        if field not in cls.search_fields:
            raise ValueError(f'Передайте в поле field одно из следующих значений {cls.__SEARCH_FIELDS}')

        result = []
        for transaction in cls.__LIST_TRANSACTIONS:
            if getattr(transaction, field, None) == keyword:
                result.append(transaction)
        return result

    def __repr__(self) -> str:
        information = {
            "pk": "pk",
            "category": 'Категория',
            "date": "Дата",
            "amount": "Сумма",
            "description": "Описание",
        }
        info = "\n".join(
            [
                f"{information[field]}: {getattr(self, field)}"
                for field in information
            ]
        )
        return f"Информация по транзакции:\n{info}"

    @classproperty
    def categories(cls) -> dict:
        """
            Геттер для search_category (main)
        """
        return cls.__CATEGORIES
