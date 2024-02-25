import pytest
from src import classes


@pytest.fixture
def category():
    return (classes.Category("fruits", "description", ["apple", "banana", "grape"]),
            classes.Category("vegetables", "description", ["cucumber", "potato", "tomato"]))


@pytest.fixture
def apple():
    return classes.Product("apple", "description", 300.50, 5)


def test_category_init(category):
    """
    Тест инициализации класса Категория
    """
    assert category[0].name == "fruits"
    assert category[0].description == "description"
    assert category[0].products == ["apple", "banana", "grape"]
    assert category[0].number_of_unique_products == 3
    assert category[1].number_of_unique_products == 3


def test_product_init(apple):
    """
    Тест инициализации класса Продукт
    """
    assert apple.name == "apple"
    assert apple.description == "description"
    assert apple.price == 300.50
    assert apple.quantity == 5


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
