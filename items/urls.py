from django.urls import path

from items.views import index, good_detail

app_name = 'items'

urlpatterns = [
    path('', index, name='index'),
    path('good_detail/<int:good_id>', good_detail, name='good-detail'),
]