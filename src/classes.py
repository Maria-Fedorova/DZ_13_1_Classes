'''Создание класса Category'''


class Category:
    # Свойства (атрибуты) класса
    name: str
    description: str
    goods: list

    # Переменные на уровне класса
    amount_of_categories = 0
    amount_of_unique_goods = 0

    '''Конструктор для инициализации экземпляра класса.
    Задаем значения атрибутам экземпляра класса'''
    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods


'''Создание класса Product'''


class Product:
    # Свойства (атрибуты) класса
    name: str
    description: str
    price: float
    amount_present: int

    '''Конструктор для инициализации экземпляра класса.
        Задаем значения атрибутам экземпляра класса'''
    def __init__(self, name, description, price, amount_present):
        self.name = name
        self.description = description
        self.price = price
        self.amount_present = amount_present