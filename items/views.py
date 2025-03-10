from django.http import HttpResponse, Http404
from django.shortcuts import render

from items.constants import DATABASE


def index(request):
    goods = DATABASE.get('goods', [])

    context = {
        'goods': goods,
    }

    return render(request, 'items/index.html', context)


def good_detail(request, good_id):
    goods = DATABASE.get('goods', [])
    good = next((item for item in goods if item.get('id') == good_id), None)

    if good is None:
        raise Http404

    context = {
        'good': good,
    }

    return render(request, 'items/good_detail.html', context)