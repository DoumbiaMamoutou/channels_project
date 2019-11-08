from django.contrib import admin
from . import models
# Register your models here.

# @admin.register(models.Chat)

class ChatAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'status', 'date_add', 'date_upd',)
    list_filter = ('status', 'date_add',)
    search_fields = ('message',)
    date_hierarchy = ('date_add',)
    list_perpage = 10

admin.site.register(models.Chat, ChatAdmin)
