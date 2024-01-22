"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


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
