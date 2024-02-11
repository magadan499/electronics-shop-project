import pytest
from src.keyboard import Keyboard


def test_str():
    """Проверяем правильный вывод имени и раскладки клавиатуры"""
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"


def test_change_lang():
    """Проверяем изменение языка клавиатуры"""
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"
