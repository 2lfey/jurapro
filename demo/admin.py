from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.Order)
admin.site.register(models.ItemInOrder)
admin.site.register(models.Cart)