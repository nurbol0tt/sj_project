from django.contrib import admin

from src.apps.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'surname', 'phone', 'created_date'
    )
    list_display_links = (
        'id', 'name',  'surname', 'phone', 'created_date'
    )
    search_fields = (
        'username',  'surname', 'phone', 'created_date'
    )
