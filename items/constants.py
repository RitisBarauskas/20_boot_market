

DATABASE = {
    'categories': [
        {
            'id': 1,
            'name': 'Категория 1',
            'description': 'Описание категории',
        },
        {
            'id': 2,
            'name': 'Категория 2',
            'description': 'Описание категории',
        }
    ],
    'manufactures': [
        {
            'id': 1,
            'name': 'Производитель 1',
            'address': 'Адрес производителя',
            'phone': '+7911236578'
        },
        {
            'id': 2,
            'name': 'Производитель 2',
            'address': 'Адрес производителя',
            'phone': '+7922236578'
        }
    ],
    'goods': [
        {
            'id': 11,
            'name': 'Товар 1',
            'description': 'Описание товара',
            'manufacture_id': 1,
            'category_id': 1,
        },
        {
            'id': 233333331,
            'name': 'Товар 2',
            'description': 'Описание товара',
            'manufacture_id': 2,
            'category_id': 1,
        },
        {
            'id': 6,
            'name': 'Товар 3',
            'description': 'Описание товара',
            'manufacture_id': 1,
            'category_id': 2,
        }
    ]
}
