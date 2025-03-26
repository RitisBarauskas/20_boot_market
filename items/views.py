from django.shortcuts import render, get_object_or_404

from items.models import Tag, Category, Manufacture, Good


def index(request):
    goods = Good.objects.all()

    context = {
        'goods': goods,
    }

    return render(request, 'items/index.html', context)


def good_detail(request, good_id):
    good = get_object_or_404(Good.objects.select_related('category', 'manufacture'), id=good_id)

    context = {
        'good': good,
    }

    return render(request, 'items/good_detail.html', context)


def goods_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    goods = category.goods.all()

    context = {
        'type': 'категории',
        'name': category.name,
        'goods': goods,
    }

    return render(request, 'items/goods_by.html', context)


def goods_by_manufacture(request, manufacture_id):
    manufacture = get_object_or_404(Manufacture, id=manufacture_id)
    goods = manufacture.goods.all()

    context = {
        'type': 'производителю',
        'name': manufacture.name,
        'goods': goods,
    }

    return render(request, 'items/goods_by.html', context)


def goods_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    goods = tag.goods.all()

    context = {
        'type': 'тегу',
        'name': tag.name,
        'goods': goods,
    }

    return render(request, 'items/goods_by.html', context)
