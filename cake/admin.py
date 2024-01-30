from django.contrib import admin
from .models import Cake


class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','quantity')



admin.site.register(Cake, CakeAdmin)


