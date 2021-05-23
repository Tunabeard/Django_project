from django.db import models

class Author(models.Model):
    name = models.CharField(
        verbose_name = "Имя или псевдоним",
        max_length = 200,
        blank = False, null = False,
    )
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Series(models.Model):
    name = models.CharField(
        verbose_name = "Серия книг",
        max_length = 200,
        blank = True, null = True,
    )
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Серия"
        verbose_name_plural = "Серии"

class Genre(models.Model):
    name = models.CharField(
        verbose_name = "Жанр",
        max_length = 80,
        blank = False, null = False,
    )
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Publisher(models.Model):
    name = models.CharField(
        verbose_name = "Издатель",
        max_length = 200,
        blank = True, null = True,
    )
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Издатель"
        verbose_name_plural = "Издатели"

# Дальше идут сугубо пробные записки
'''
class PriceUnits(models.Model):
    name = models.CharField(
        default = "usd",
        verbose_name = "Название",
        max_length = 40,
        blank = False, null = False,
    )

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Валюта",
        verbose_name_plural = "Валюты",

class Book(models.Model):
    name = models.CharField(
        verbose_name = "Название",
        default = "default_title",
        max_length = 100,
        blank = False, null = False,
    )
    # image = models.ImageField()
    price = models.FloatField(
        verbose_name = "Цена",
        blank = False, null = False,
    )
    # price_unit = models.ForeignKey(PriceUnits, on_delete = models.PROTECT, related_name = "products",)
    description = models.TextField(
        verbose_name = "Описание",
        max_length = 800,
        blank = True, null = True,
    )
    created = models.DateTimeField(
        verbose_name = "Дата внесения",
        auto_now = False, auto_now_add = True,
    )
    updated = models.DateTimeField(
        verbose_name = "Дата последнего редактирования",
        auto_now = True, auto_now_add = False,
    )

    def __str__(self) -> str:
        return f"Товар {self.name}"
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
'''