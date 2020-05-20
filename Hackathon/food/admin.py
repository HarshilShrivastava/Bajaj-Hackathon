from django.contrib import admin
from food.models import (
    Food
)
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Food)
class PersonAdmin(ImportExportModelAdmin):
    pass
# Register your models here.
