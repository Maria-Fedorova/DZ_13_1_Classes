import pytest
from src import classes, utils


@pytest.fixture
def category():
    return (classes.Category("fruits", "description", ["apple", "banana", "grape"]),
            classes.Category("vegetables", "description", ["cucumber", "potato", "tomato"]))


@pytest.fixture
def fruits():
    return (classes.Product("apple", "apple_description", 300.50, 5),
            classes.Product("pear", "pear_description", 100.50, 17))


def test_category_init(category):
    """
    Тест инициализации класса Категория
    """
    assert category[0].name == "fruits"
    assert category[0].description == "description"
    assert category[0]._Category__products == ["apple", "banana", "grape"]
    assert category[0].number_of_unique_products == 3
    assert category[1].number_of_unique_products == 3


def test_products():
    """
    1. Тест геттера, который выводит список товаров в формате:
    Продукт, 80 руб. Остаток: 15 шт.
    2. Тест сеттера, который добавляет товары
    """
    x = utils.load_data('products.json')
    y = utils.create_objects_category_product(x)
    assert y[0][0].products == (f'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                f'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                f'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.')
    assert y[0][0].number_of_unique_products == 3
    y[0][0].products = classes.Product(name="pear", description="pear_description", price=100.50, quantity=17)
    assert y[0][0].products == (f'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                f'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                f'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n'
                                f'pear, 100.5 руб. Остаток: 17 шт.')
    assert y[0][0].number_of_unique_products == 4


def test__len__cat():
    """
    Проверка вывода количества продуктов на складе
    """
    x = utils.load_data('products.json')
    y = utils.create_objects_category_product(x)
    assert len(y[0][0]) == 27
    assert len(y[0][1]) == 7


def test__str__cat():
    """
    Проверка для класса Category: добавляет строковое отображение в следующем виде:
    "Название категории, количество продуктов: 200 шт."
    """
    x = utils.load_data('products.json')
    y = utils.create_objects_category_product(x)
    assert str(y[0][0]) == f'{y[0][0].name}, количество продуктов: {len(y[0][0])} шт.'
    assert str(y[0][1]) == f'{y[0][1].name}, количество продуктов: {len(y[0][1])} шт.'


def test_product_init(fruits):
    """
    Тест инициализации класса Продукт
    """
    assert fruits[0].name == "apple"
    assert fruits[0].description == "apple_description"
    assert fruits[0].price == 300.50
    assert fruits[0].quantity == 5


def test_create_product():
    """
    Проверка создания товара и возврата объекта
    """
    assert (str(classes.Product.create_product(
        {"name": "mango", "description": "mango_description", "price": 5.0, "quantity": 5})) ==
            str(classes.Product(name="mango", description="mango_description", price=5.0, quantity=5)))


def test__str__prod(fruits):
    """
    Проверка для класса Product: добавляет строковое отображение в следующем виде:
    "Название продукта, 80 руб. Остаток: 15 шт."
    """
    assert str(fruits[0]) == f'{fruits[0].name}, {fruits[0].price} руб. Остаток: {len(fruits[0])} шт.'


def test__add__prod(fruits):
    assert fruits[0] + fruits[1] == fruits[0].price * fruits[0].quantity + fruits[1].price * fruits[1].quantity


def test_price(fruits):
    """
    Проверка геттера, сеттера и делитера цены
    """
    assert fruits[0].price == 300.5
    fruits[0].price = 100.0
    assert fruits[0].price == 100.0
    fruits[0].price = -1
    assert fruits[0].price <= 0, "Цена введена некорректная"
    del fruits[0].price
    assert fruits[0].price is None


def test_number_of_categories(category):
    """
    Тест на провеоку подсчёта количества категорий
    """
    assert category[0].number_of_categories == 1
    assert category[1].number_of_categories == 1


def test_number_of_unique_products(category):
    """
    Тест на провеоку подсчёта количества продуктов
    """
    assert category[0].number_of_unique_products == 3
    assert category[1].number_of_unique_products == 3