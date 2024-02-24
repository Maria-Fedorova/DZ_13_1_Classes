class Category:

    '''Создание класса Category'''

    # Свойства (атрибуты) класса
    name: str
    description: str
    products: list

    # Переменные на уровне класса
    number_of_categories = 0


    def __init__(self, name, description, products):
        '''Конструктор для инициализации экземпляра класса.
        Задаем значения атрибутам экземпляра класса'''
        self.name = name
        self.description = description
        self.products = products

        Category.number_of_categories += 1

    def __repr__(self):
        return f'name={self.name}, description={self.description}, products={self.products})'

class Product:

    '''Создание класса Product'''

    # Свойства (атрибуты) класса
    name: str
    description: str
    price: float
    quantity: int

    # Переменные на уровне класса
    number_of_unique_products = 0


    def __init__(self, name, description, price, quantity):
        '''Конструктор для инициализации экземпляра класса.
            Задаем значения атрибутам экземпляра класса'''
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.number_of_unique_products += 1

    def __repr__(self):
        return f'name={self.name}, description={self.description}, price={self.price}, number_present={self.quantity})'
