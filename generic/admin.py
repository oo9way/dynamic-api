from django.contrib import admin
from generic.models import GenericAPI, GenericAPIField


class GenericAPIFieldInline(admin.TabularInline):
    list_display = ('id', 'name', 'field_type', 'is_searchable')
    model = GenericAPIField


@admin.register(GenericAPI)
class GenericAPIAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "add_view", "list_view", "detail_view", "update_view", "delete_view", "use_cache",
                    "cache_time", "authorization_required", "permission_required", "pagination", "counter", "throttle",
                    "throttle_time")

    inlines = (GenericAPIFieldInline,)
