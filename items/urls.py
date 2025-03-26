from django.urls import path

from items.views import index, good_detail, goods_by_category, goods_by_manufacture, goods_by_tag

app_name = 'items'

urlpatterns = [
    path('', index, name='index'),
    path('good_detail/<int:good_id>', good_detail, name='good-detail'),
    path('goods_by_category/<int:category_id>', goods_by_category, name='goods-by-category'),
    path('goods_by_manufacture/<int:manufacture_id>', goods_by_manufacture, name='goods-by-manufacture'),
    path('goods_by_tag/<int:tag_id>', goods_by_tag, name='goods-by-tag'),
]