## Финансовый кошелек на классах.

---

## Тех.детали:
* datetime, 
* re, 
* from 
* typing 
* import Union, 
* filter, 
* map, 
* lambda, 
* while True (continue), 
* globals()
<br/><br/>
<hr>


## Описание:
**Закрепляю ООП. Проект-финансовый кошелек, который написан на классах.** 

После запуска (main.py) выводится меню (+баланс кошелька)<br/><br/>
            -- Меню --
1.  Показать баланс
2. Показать доходы
3. Показать расходы
4. Новая транзакция (запросит: pk, Дата, Категория, Сумма, Описание)
5. Поиск по транзакциям (будет предложен поиск по: Дате, Сумме, Категории)
6. Показать все транзакции
Баланс кошелька: 500.0
<br/><br/>
<hr>


## Архитектура:

**models/stream.py**
<dd>class Stream инициализируется при запуске проекта. Создает директоию 'local_user.csv'
    с файлом 'local_user.csv' с заголовками ( pk | date | category | amount | description ).</dd>   

В процессе работы кошелька:
  * читает, записывает данные в 'local_user.csv'
  * обменивается данными с class Transaction
<br/><br/>


   
    
**models/transaction.py**
<dd> class Transaction. Инициализируется при запуске проекта. Создает рабочий операционный фаил __LIST_TRANSACTIONS.</dd>

В процессе работы кошелька:
  * создание транзакции, дозапись, чтение транзакции, валидация данных.
  * итерирует данные для получения (доходов, расходов, баланса, поиска по транзакциям)
  * передает данные в class Stream для записи в 'local_user.csv'
<br/><br/>

**er-model .drawio.png** - графическая модель проекта
<br/><br/>

**main.py**  <dd>Запуск проекта.</dd>
В процессе работы кошелька:
  * выводит меню пользователю
  * принимает и валидирует данные у пользователя (для Раздела поиск 1.Date 2.Amount 3.Category,
         для вывода доходов, расходов и т.д)
<br/><br/>
             
**utils.py** - Рукописный декоратор. Использую его в class Transaction.list_transactions в геттере.
        Гибрид @property + @classmethod
<br/><br/>
<hr>
        


## Особенности:
Плотно закрепил ООП:

- **self** передается первым аргументом в метод класса и представляет собой ссылку на
экземпляр класса. Используется для доступа к атрибутам и методам экземпляра из
методов класса. 
- **cls** (ссылка на класс) метод класса, а не экземпляра класса! и обращается к классу
 и используется в методах класса, обозначенных декоратором **@classmethod**.
С его помощью можно управлять атрибутами, присущими классу. 
                
- **атрибуты** (свойства) класса (статические & локальные ) переменные внутри класса

- **__private** (приватные [двойное нижнее подчеркивание]) методы доступны только внутри
класса, 
- **_protected** (защищенные) — внутри класса и в дочерних классах. Говорит разрабу,
 что бы он не лез!
- **public** по умолчанию (без подчеркивания) все методы, локальные сво-ва, статические
свойства имеют уровень доступа 
- если стоит **@staticmethod**: этот метод можно вызывать откуда угодно

      
- **Инкапсуляция** — ограничение доступа к составляющим объект компонентам (методам и
переменным). Инкапсуляция делает некоторые из компонент доступными только внутри
класса.
- **Наследование** - перенимаем все св-во (локальные, статические), методы, базового
 класса (приватные св-ва, методы НЕ НАСЛЕДУЮТСЯ)
- **Полиморфизм** - способность объекта вести себя по разному, в зависимости от, того,
 от какого экземпляра класса он создан. Полиморфизм - разное поведение одного и 
 того же метода в разных классах.


- **@property** - условно Вызов функции без скобок, но я не могу передать в функцию
 аргументы
 
- Метод **__repr__()** возвращает информативное (официальное) строковое представление
 объекта.
 
- Практика в написании валидаций (даты, наличия переменной в списке, 
может ли переменная быть int() or float() or str(), )

- **globals()** - функция globals() возвращает словарь со всеми глобальными переменными и
 символами для текущей программы.
- Аннотации типов.
- Использовал блок **try, except**.
- Переписал на генераторы списка.
<br/><br/>
<hr>
        
                


## Что бы установить и запустить проект:
Создать директорию на компьютере  
Открыть нужный репозиторий -> Code -> HTTPS -> скопировать ссылку
```python
$ git clone + ссылка 
```
Перейти в паку с проектом, запустить main.py
<br/><br/>
<hr>


![alt-текст](https://github.com/HeyArtem/Financial-wallet-on-classes/blob/main/picture%20for%20readme/11.png "Baner") 
![alt-текст](https://github.com/HeyArtem/Financial-wallet-on-classes/blob/main/picture%20for%20readme/12.png "Baner2")
![alt-текст](https://github.com/HeyArtem/Financial-wallet-on-classes/blob/main/picture%20for%20readme/13.png "Baner3")
