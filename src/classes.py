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
            list_product.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
        return "\n".join(list_product)

    @products.setter
    def products(self, new_product):
        """
        Добавляет продукт в категорию
        """
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            self.number_of_unique_products += 1
        else:
            raise TypeError("Добавлять можно только Продукты и дочение классы")

    def __len__(self):
        """
        Вывод количества продуктов на складе
        """
        num_all_products = 0
        for product in self.__products:
            num_all_products += product.quantity
        return num_all_products


    def __str__(self):
        """
        Для класса Category добавляет строковое отображение в следующем виде:
        "Название категории, количество продуктов: 200 шт."
        """
        #return f'{self.name}, количество продуктов:  шт.'
        return f'{self.name}, количество продуктов: {len(self)} шт.'

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
    def create_product(cls, product_data):
        """
        Создает товар и возвращает объект, который можно добавлять в список товаров
        """
        return cls(**product_data)


    def __len__(self):
        """
        Возвращает количество оставшихся товаров конкретного вида (продукта)
        По сути это self.quantity. Написано только ради использования метода __len__
        """
        return self.quantity


    def __str__(self):
        """
        Для класса Product добавляет строковое отображение в следующем виде:
        "Название продукта, 80 руб. Остаток: 15 шт."
        """
        return f'{self.name}, {self.price} руб. Остаток: {len(self)} шт.'

    def __add__(self, other):
        """
        Сложение объектов между собой
        """
        if type(self) != type(other):
            raise TypeError('Складывать можно только объекты одного типа.')
        return self.price * self.quantity + other.price * other.quantity

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


class Smartphone(Product):

    # Свойства (атрибуты) класса
    performance: float
    model: str
    built_in_memory: int
    color: str

    def __init__(self, name, description, price, quantity, performance, model, built_in_memory, color):
        """Конструктор для инициализации экземпляра класса.
            Задаем значения атрибутам экземпляра класса"""
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.built_in_memory = built_in_memory
        self.color = color


class LawnGrass(Product):

    # Свойства (атрибуты) класса
    manufacturer_country: str
    germination_period: float
    color: str

    def __init__(self, name, description, price, quantity, manufacturer_country, germination_period, color):
        """Конструктор для инициализации экземпляра класса.
            Задаем значения атрибутам экземпляра класса"""
        super().__init__(name, description, price, quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color