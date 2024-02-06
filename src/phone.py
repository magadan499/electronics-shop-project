from item import Item


class Phone(Item):
    """Дочерний класс от класса Item."""
    def __init__(self, name: str, price: float, quantity: int, sim: int):
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param sim: Количество сим-карт в телефоне.
        """
        super().__init__(name, price, quantity)
        self.__sim = sim

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.__sim})"



