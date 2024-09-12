from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='catalog/photo', blank=True, null=True)
    price = models.IntegerField(verbose_name='цена')
    creation_date = models.DateField(blank=True, null=True, verbose_name='дата создания')
    last_mod_date = models.DateField(blank=True, null=True, verbose_name='дата последнего изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title', 'category']

    def __str__(self):
        return self.title
