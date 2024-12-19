from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "status"]
    list_filter = ["status", "created_at"]
    ordering = ["-created_at", "-updated_at"]
    search_fields = ["title", "body"]
