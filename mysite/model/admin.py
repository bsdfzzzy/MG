from django.contrib import admin
from models import *

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'system_id', 'event', 'date')
    date_hierarchy = 'date'

class BaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'system_id', 'subsystem', 'date', 'supervisor_1', \
                'supervisor_2', 'supervisor_3', 'respector', 'experiment', 'IP', \
                'type', 'work', 'category', 'stateOrDate', 'More')
    date_hierarchy = 'date'

class BizAdmin(admin.ModelAdmin):
    list_display = ('id', 'system_id', 'column', 'playStart', \
                'playFinish', 'numOfNeeds', 'allReadyTime', 'state')

admin.site.register(Base, BaseAdmin)
admin.site.register(Biz, BizAdmin)
admin.site.register(Event, EventAdmin)