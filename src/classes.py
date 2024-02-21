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


'''Создание класса Product'''


class Product:
    # Свойства (атрибуты) класса
    name: str
    description: str
    price: float
    amount_present: int

    # Переменные на уровне класса
    number_of_unique_products = 0

    '''Конструктор для инициализации экземпляра класса.
        Задаем значения атрибутам экземпляра класса'''
    def __init__(self, name, description, price, number_present):
        self.name = name
        self.description = description
        self.price = price
        self.number_present = number_present

        Product.number_of_unique_products += 1

    category_1 = Category('fruits', 'description', ["apple", "banana", "grape"])
    product_1 = Product("apple", "description", 300.50, 5)

    print(Category.number_of_categories)
