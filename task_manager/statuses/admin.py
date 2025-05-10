from django.contrib import admin
from .models import Status


# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    pass


admin.site.register(Status, StatusAdmin)