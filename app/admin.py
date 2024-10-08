from django.contrib import admin
# # Register your models here.
# admin.site.register(Blog)


from django.contrib import admin
from django.contrib import admin
from .models import *

admin.site.register(ContactData)
admin.site.register(Contact)

# admin.site.register(News)
# admin.site.register(Category)
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status', 'category']
    list_filter = ['status', 'created_time', 'publish_time']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['']
    ordering = ['title',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
#


