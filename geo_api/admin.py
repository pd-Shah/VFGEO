from django.contrib import admin

from .models import Municipality

BASE = ["description", "created_at", "updated_at", ]


@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    list_filter = [] + BASE
    list_display = ["title", ] + BASE
