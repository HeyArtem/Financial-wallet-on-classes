import csv
import os

from models.transaction import Transaction


class Stream:
    PATH_FOLDER = 'transactions_data'
    FILE_NAME = 'local_user.csv'
    FIELDS_TRANSACTION = {
        'pk': int,
        'date': str,
        'category': str,
        'amount': float,
        'description': str,
    }

    def __init__(self) -> None:
        self.__initialization()

    @classmethod
    def path(cls) -> str:
        """
            Возвращает путь до файла с транзакциями
        """
        return f"{cls.PATH_FOLDER}/{cls.FILE_NAME}"

    @classmethod
    def __initialization(cls) -> None:
        """
            Создает папку и фаил д\хранения транзакций с заголовками
        """

        if not os.path.exists(cls.PATH_FOLDER):
            os.mkdir(cls.PATH_FOLDER)

        with open(cls.path(), mode='a') as file:
            if os.stat(cls.path()).st_size == 0:
                writer = csv.DictWriter(file, fieldnames=cls.FIELDS_TRANSACTION.keys())
                writer.writeheader()

    @classmethod
    def read(cls) -> list:
        """
            Читает существующие сохраненные транзакции,
            возвращает список транзакций в виде словарей
        """
        transactions = []
        with open(cls.path(), newline='') as file:
            for row in csv.DictReader(file):
                transactions.append({
                    key: cls.FIELDS_TRANSACTION[key](value)
                    for key, value in row.items()
                })
        return transactions

    def write(self, transaction: Transaction) -> None:
        """
            Принимает экз-р класса Transaction.
            Записывает транзакцию.
        """
        data = [
            getattr(transaction, field)
            for field in self.FIELDS_TRANSACTION.keys()
        ]
        with open(self.path(), 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)
