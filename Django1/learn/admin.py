from django.contrib import admin
from learn.models import train_course, train, train_basic


class TrainAdmin(admin.ModelAdmin):
    list_display = ('Course', 'People', 'Teacher', 'Section', 'Place', 'Classes', 'Week')


class BasicAdmin(admin.ModelAdmin):
    list_display = ('id', 'Pastern', 'Build', 'Content', 'Name', 'Power', 'Area')


admin.site.register(train_course, TrainAdmin)
admin.site.register(train)
admin.site.register(train_basic, BasicAdmin)
