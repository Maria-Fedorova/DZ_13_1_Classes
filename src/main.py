import utils


def main():
    """
    Создание объектов класса
    """
    data = utils.load_data('products.json')
    utils.create_objects_category_product(data)


if __name__ == '__main__':
    main()
