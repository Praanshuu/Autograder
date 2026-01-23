from django.contrib import admin
from .models import Class, Enrollment, Module


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'section', 'owner', 'join_code', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'section']
    readonly_fields = ['join_code']


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'class_obj', 'order_index']
    list_filter = ['class_obj']
    ordering = ['class_obj', 'order_index']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'class_obj', 'role', 'joined_at']
    list_filter = ['role', 'joined_at']
    search_fields = ['user__username', 'class_obj__name']
