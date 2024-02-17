"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError
from config import ITEMS
from src.phone import Phone


def test_calculate_total_price():
    """Проверяем расчёт общей стоимости"""
    item1 = Item("Ключ", 100, 20)
    assert item1.calculate_total_price() == 2000


def test_apply_discount():
    """Проверяем стоимость с учетом скидки"""
    item1 = Item("Ключ", 100, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 80


def test_name():
    """Тест проверки длины наименования товара (не больше 10 символов)"""
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"
    item1.name = "Духовой шкаф"
    assert item1.name == "Духовой шк"


def test_instantiate_from_csv():
    """Проверка добавления экземпляров класса из CSV файла"""
    Item.instantiate_from_csv(ITEMS)
    assert len(Item.all) == 5


def test_string_to_number():
    """Проверка возвращения числа из строки-числа"""
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("1.5") == 1


def test_repr():
    """Проверка вывода информации о товаре"""
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    """Проверка наименования"""
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    """Проверка сложения количества единиц техники экземпляров класса"""
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_instantiate_from_csv_not():
    """Проверяет на наличие файла"""
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(" ")
