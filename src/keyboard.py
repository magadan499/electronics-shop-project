from src.item import Item


class LangMixin:
    """Миксин, изменяет раскладку клавиатуры"""
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        """Получает доступ к приватному аттрибуту класса"""
        return self.__language

    def change_lang(self):
        """Изменение раскладки клавиатуры (смена языка)"""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(Item, LangMixin):
    """Класс наследуется от класса Item, имеет дополнительный аттрибут (раскладку клавиатуры),
    а также метод по изменению этой раскладки"""
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        LangMixin.__init__(self)
