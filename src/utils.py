import os
import json
import classes


def load_data(filename):
    """
    Загружает информацию из файла
    """
    with open(file=os.path.abspath(filename), mode='r', encoding='utf-8') as file:
        return json.load(file)


def create_objects_category(data):
    new_category = []
    new_product = []
    for object in data:
        if len(data) != 0:
            category = classes.Category(object['name'], object['description'], object['products'])
            new_category.append(category)
            #product = classes.Product(object['products']['name'], object['products']['description'], object['products']['price'], object['products']['quantity'])
            #new_product.append(product)
    print(new_category)
    print(new_product)
    return new_category, #new_product
#print(create_objects_category(load_data('products.json')))
#print(create_objects_category(load_data('products.json'))[1])



def main():
    """
    Создание объектов класса
    """
    data = load_data('products.json')
    create_objects_category(data)

main()
