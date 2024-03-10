class Category:

    """Создание класса Category"""

    # Свойства (атрибуты) класса
    name: str
    description: str
    products: list

    # Переменные на уровне класса
    number_of_categories = 0
    number_of_unique_products = 0

    def __init__(self, name, description, products):
        """Конструктор для инициализации экземпляра класса.
        Задаем значения атрибутам экземпляра класса"""
        self.name = name
        self.description = description
        self.__products = products
        self.number_of_unique_products += len(self.__products)
        self.number_of_categories += 1

    @property
    def products(self):
        """Геттер, который выводит список товаров в формате:
        Продукт, 80 руб. Остаток: 15 шт."""
        list_product = []
        for product in self.__products:
            list_product.append(f'{product["name"]}, {product["price"]} руб. Остаток: {product["quantity"]} шт.')
        return "\n".join(list_product)

    def __repr__(self):
        return f'name={self.name}, description={self.description}, products={self.__products})'


class Product:

    """Создание класса Product"""

    # Свойства (атрибуты) класса
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Конструктор для инициализации экземпляра класса.
            Задаем значения атрибутам экземпляра класса"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name, description, price, quantity):
        """
        Создает товар и возвращает объект, который можно добавлять в список товаров
        """
        return {"name": name, "description": description, "price": price, "quantity": quantity}

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректная")
        self.__price = new_price

    @price.deleter
    def price(self):
        self.__price = None

    def __repr__(self):
        return f'name={self.name}, description={self.description}, price={self.price}, number_present={self.quantity})'
