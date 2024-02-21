import pytest
from src import classes


@pytest.fixture
def fruits():
    return classes.Category("apple", "description", ["apple", "banana", "grape"])
def test_category_init(fruits):
    assert fruits.name == "apple"
    assert fruits.description == "description"
    assert fruits.goods == ["apple", "banana", "grape"]
