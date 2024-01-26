"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from config import ITEMS


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
