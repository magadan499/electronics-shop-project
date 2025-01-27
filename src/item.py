import csv


class InstantiateCSVError(Exception):
    """Выбрасывает исключение если файл поврежден или отсутствует одна из колонок данных"""
    def __init__(self, *args, **kwargs):
        self.message = 'Данный файл поврежден'

    def __str__(self):
        return self.message


class Item:
    """Класс для представления товара в магазине."""
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        """Складываем экземпляры класса родителя и дочерних классов
        по количеству единиц quantity"""
        if isinstance(other, Item):
            return int(self.quantity) + int(other.quantity)
        else:
            return None

    def calculate_total_price(self) -> float:
        """Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара."""
        return self.price * self.quantity

    def apply_discount(self):
        """Применяет установленную скидку для конкретного товара."""
        self.price *= self.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """Проверяем, что длина наименования товара не больше 10 символов"""
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        """Добавление экземпляров класса из CSV файла"""
        try:
            cls.all = []
            with open(csv_file, encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls(str(row['name']), float(row['price']), int(row['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {csv_file} отсутствует")
        except KeyError:
            raise InstantiateCSVError

    @staticmethod
    def string_to_number(str_number):
        """Возвращает число из строки-числа"""
        number = float(str_number)
        return int(number)
