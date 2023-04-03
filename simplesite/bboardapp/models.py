from django.db import models


class Bb(models.Model):
    STATUS_CHOICES = [
        ('Go', 'Хорошее'),
        ('No', 'Среднее'),
        ('Bad', 'Плохое'),
    ]
    title = models.CharField(max_length=50, verbose_name='Название')
    text = models.TextField(null=True, blank=True, verbose_name='Описание')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Go',
                              verbose_name='Состояние')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT,
                               verbose_name='Категория')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']
