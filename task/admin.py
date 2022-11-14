from django.contrib import admin
from .models import book
@admin.register(book)

class bookAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ("id","a_name","name","price")
    list_filter = ("id","a_name","name","price")
    search_fields = ("name","a_name")

