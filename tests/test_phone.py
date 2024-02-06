from src.phone import Phone


def test_str():
    """Проверка наименования"""
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'

def test_repr():
    """Проверка вывода информации о товаре"""
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
