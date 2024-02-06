from src.item import Item


class Phone(Item):
    """Дочерний класс от класса Item."""
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество сим-карт в телефоне.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        """Получаем доступ к приватному значению количества сим-карт"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, quantity):
        """Проверяем, что число сим-карт не может быть нулевым или меньше."""
        if quantity <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        else:
            self.__number_of_sim = int(quantity)
