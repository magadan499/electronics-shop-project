"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def calculate_total_price():
    """Проверяем рассчёт общей стоимости"""
    item1 = Item("Ключ", 100, 20)
    assert item1.calculate_total_price() == 2000
