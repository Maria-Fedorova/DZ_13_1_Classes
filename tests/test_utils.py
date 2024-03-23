from src import utils


def test_load_data():
    """
    Тестирует загрузку данных из json файла
    """
    x = utils.load_data('products.json')
    assert len(x) != 0
    assert type(x) is list
    assert type(x[0]) is dict


def test_create_objects_category_product():
    """
    Тестирует создание объектов класса Категория
    """

    x = utils.load_data('products.json')
    y = utils.create_objects_category_product(x)
    assert len(y[0]) == 2
    assert len(y[1]) == 4
