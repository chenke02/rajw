from django.contrib import admin
from .models import train_course, train_basic


class TrainAdmin(admin.ModelAdmin):
    list_display = ('Course', 'People', 'Teacher', 'Section', 'Place', 'Classes', 'Week')


class BasicAdmin(admin.ModelAdmin):
    list_display = ('uid',  'Category', 'Pastern', 'Build', 'Content', 'Name', 'Power', 'Length', 'Width', 'Remarks')


admin.site.register(train_course, TrainAdmin)
admin.site.register(train_basic, BasicAdmin)
