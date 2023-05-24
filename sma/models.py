from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField('Наименование продукции', max_length=70)

    class Meta:
        ordering = ['id']
        verbose_name = 'Продукцию'
        verbose_name_plural = 'Тип продукции'

    def __str__(self):
        return self.title


class Equipment(models.Model):
    title = models.CharField('Наименование оборудования', max_length=100)
    product = models.ForeignKey(Product, verbose_name='Тип продукции', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'

    def __str__(self):
        return self.title


class Model(models.Model):
    title = models.CharField('Наименование модели', max_length=70)
    equipment = models.ForeignKey(Equipment, verbose_name='Тип оборудования', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['id']
        verbose_name = 'Модель'
        verbose_name_plural = 'Модель оборудования'

    def __str__(self):
        return self.title


class ServiceType(models.Model):
    title = models.CharField('Наименование вида услуги', max_length=70)

    class Meta:
        ordering = ['id']
        verbose_name = 'Вид услуг'
        verbose_name_plural = 'Виды услуг'

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField('Наименование услуги', max_length=70)
    service_type = models.ForeignKey(ServiceType, verbose_name='Вид услуг', on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(Model, verbose_name='Модель оборудования', on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(
        'Количество, шт.',
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    discount = models.IntegerField(
        'Размер скидки',
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        null=True,
        blank=True,
        help_text='В процентах'
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'

    def display_amount(self):
        amount = self.model.price * self.count

        if self.discount:
            amount = round(amount * Decimal(1 - self.discount.value / 100))
        return '{0} тг.'.format(amount)

    def __str__(self):
        return self.title

    def value_percent(self):
        if self.discount:
            return str(self.discount) + '%'

    value_percent.short_description = 'Размер скидки'
    display_amount.short_description = 'Сумма'


class GrCostItem(models.Model):
    title = models.CharField('Наименование элемента затрат', max_length=70)

    class Meta:
        ordering = ['id']
        verbose_name = 'Элемента затрат'
        verbose_name_plural = 'Элементы затрат'

    def __str__(self):
        return self.title


class CostItem(models.Model):
    title = models.CharField('Наименование статьи затрат', max_length=100)
    gr_cost_item = models.ForeignKey(GrCostItem, verbose_name='Элемент затрат', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Статью затрат'
        verbose_name_plural = 'Статьи затрат'

    def __str__(self):
        return self.title


class Measure(models.Model):
    title = models.CharField('Наименование единицы измерения', max_length=70)

    class Meta:
        ordering = ['id']
        verbose_name = 'Единицу измерения'
        verbose_name_plural = 'Единицы измерения'

    def __str__(self):
        return self.title


class Indicator(models.Model):
    title = models.CharField('Наименование показателя', max_length=70)
    measure = models.ForeignKey(Measure, verbose_name='Единица измерения', on_delete=models.SET_NULL, null=True)
    value = models.DecimalField('Значение', max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Показатель'
        verbose_name_plural = 'Показатели'

    def __str__(self):
        return self.title
