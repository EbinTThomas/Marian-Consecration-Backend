from django.contrib import admin
from .models import Consecration, Day, UserProgress

@admin.register(Consecration)
class ConsecrationAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date')
    list_filter = ('start_date',)
    search_fields = ('title',)

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('day_number', 'prayers')

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'completed')
    list_filter = ('user', 'day', 'completed')
    search_fields = ('user__username', 'day__consecration__title')
