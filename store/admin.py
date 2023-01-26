from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order




class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminOrder(admin.ModelAdmin):
    list_display = ['product', 'customer', 'price']


# Register your models here.
@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['name', 'price', 'category']
    pass


admin.site.register(Category, AdminCategory)

@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ['name']
    pass

admin.site.register(Order, AdminOrder)