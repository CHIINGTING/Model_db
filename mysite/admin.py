from django.contrib import admin

# Register your models here.
from django.contrib import admin
from mysite import models

admin.site.register(models.Maker)
admin.site.register(models.PModel)


class pouductAdmin(admin.ModelAdmin):
    list_display = ('pmodel', 'nickname', 'price', 'year')
    search_fields = ('nickname', 'description',)
    ordering = ('-price',)


class photoAdmin(admin.ModelAdmin):
    list_display = ('product', 'description')


admin.site.register(models.Product, pouductAdmin)
admin.site.register(models.PPhoto, photoAdmin)
