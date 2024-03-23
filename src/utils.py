import os
import json
import src.classes


def load_data(filename):
    """
    Загружает информацию из файла
    """
    with open(file=os.path.abspath(filename), mode='r', encoding='utf-8') as file:
        return json.load(file)


def create_objects_category_product(data):
    """
    Создает объекты
    """
    new_category = []
    new_product = []
    for object in data:
        if len(data) != 0:
            category = src.classes.Category(object['name'], object['description'], [])
            for i_product in object['products']:
                product = src.classes.Product(i_product['name'], i_product['description'], i_product['price'],
                                              i_product['quantity'])
                new_product.append(product)
                category.products = product
            new_category.append(category)
    return new_category, new_product
