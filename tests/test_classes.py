import pytest
#import src
from src import classes


@pytest.fixture
def fruits():
    return classes.Category("fruits", "description", ["apple", "banana", "grape"])
@pytest.fixture
def apple():
    return classes.Product("apple", "description", 300.50, 5)
def test_category_init(fruits):
    assert fruits.name == "fruits"
    assert fruits.description == "description"
    assert fruits.products == ["apple", "banana", "grape"]

def test_product_init(apple):
    assert apple.name == "apple"
    assert apple.description == "description"
    assert apple.price == 300.50
    assert apple.number_present == 5

def test_number_of_categories():
    assert classes.Category.number_of_categories == 1

def test_number_of_unique_products():
    assert classes.Product.number_of_unique_products == 0
