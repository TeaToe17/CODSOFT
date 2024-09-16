from django.contrib import admin

from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name","number",)
    search_fields = ("name","number",)
    