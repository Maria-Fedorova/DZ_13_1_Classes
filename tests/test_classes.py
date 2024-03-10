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
    Тест геттера, который выводит список товаров в формате:
    Продукт, 80 руб. Остаток: 15 шт.
    """
    x = utils.load_data('products.json')
    y = utils.create_objects_category_product(x)
    assert y[0][0].products == (f'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                f'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                f'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.')


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
    Проверка создания товара
    """
    assert (classes.Product.create_product(name="mango", description="mango_description", price=5.0, quantity=5) ==
            {"name": "mango", "description": "mango_description", "price": 5.0, "quantity": 5})


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
