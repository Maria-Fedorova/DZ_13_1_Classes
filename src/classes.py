'''Создание класса Category'''


class Category:
    # Свойства (атрибуты) класса
    name: str
    description: str
    products: list

    # Переменные на уровне класса
    number_of_categories = 0

    '''Конструктор для инициализации экземпляра класса.
    Задаем значения атрибутам экземпляра класса'''
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.number_of_categories += 1

    def __repr__(self):
        return f'name={self.name}, description={self.description}, products={self.products})'


'''Создание класса Product'''


class Product:
    # Свойства (атрибуты) класса
    name: str
    description: str
    price: float
    quantity: int

    # Переменные на уровне класса
    number_of_unique_products = 0

    '''Конструктор для инициализации экземпляра класса.
        Задаем значения атрибутам экземпляра класса'''
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.number_of_unique_products += 1

    def __repr__(self):
        return f'name={self.name}, description={self.description}, price={self.price}, number_present={self.quantity})'

category_1 = Category('fruits', 'description', ["apple", "banana", "grape"])
category_2 = Category('vegetables', 'description', ["cucumber", "potato", "tomato"])
product_1 = Product('apple', 'description', 300.50, 5)
product_2 = Product('tomato', 'description', 20.50, 3)

print(type(category_1))
