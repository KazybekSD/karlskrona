from django.contrib import admin

from sma.models import Product, Equipment, Model, ServiceType, Service, CostItem, Indicator, Measure


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'product')
    list_filter = ('product',)


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'equipment', 'price')
    list_filter = ('equipment',)


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'service_type', 'model', 'count', 'value_percent', 'display_amount')
    list_filter = ('service_type', 'model')


@admin.register(CostItem)
class CostItemAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'measure')
    list_filter = ('measure', )

