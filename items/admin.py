from django.contrib.admin import register, ModelAdmin

from items.models import Tag, Category, Manufacture, Good


@register(Tag)
class TagAdmin(ModelAdmin):
    pass


@register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@register(Manufacture)
class ManufactureAdmin(ModelAdmin):
    pass


@register(Good)
class GoodAdmin(ModelAdmin):
    pass
