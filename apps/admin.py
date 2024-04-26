from django.contrib import admin

from apps.models import Student


@admin.register(Student)
class StuAdmin(admin.ModelAdmin):
    pass