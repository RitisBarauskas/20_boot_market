from django.db import models

from items.constants import MAX_LENGTH_CHAR_FIELD, MAX_LENGTH_PHONE_NUMBER

class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=MAX_LENGTH_CHAR_FIELD)
    description = models.CharField(verbose_name='Описание', max_length=MAX_LENGTH_CHAR_FIELD)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Manufacture(models.Model):
    name = models.CharField(verbose_name='Название', max_length=MAX_LENGTH_CHAR_FIELD)
    address = models.TextField(verbose_name='Адрес')
    phone = models.CharField(verbose_name='Телефон', max_length=MAX_LENGTH_PHONE_NUMBER)
    latest_update = models.DateTimeField(verbose_name='Последнее обновление')

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name


class Tag(models.Model):
    color = models.CharField(verbose_name='Цвет', max_length=MAX_LENGTH_CHAR_FIELD)
    name = models.CharField(verbose_name='Название', max_length=MAX_LENGTH_CHAR_FIELD)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(verbose_name='Название', max_length=MAX_LENGTH_CHAR_FIELD)
    description = models.CharField(verbose_name='Описание', max_length=MAX_LENGTH_CHAR_FIELD)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='goods',
        blank=True,
        null=True,
        verbose_name='Категория',
    )
    manufacture = models.ForeignKey(
        Manufacture,
        on_delete=models.SET_NULL,
        related_name='goods',
        blank=True,
        null=True,
        verbose_name='Производитель',
    )
    tags = models.ManyToManyField(Tag, related_name='goods')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
