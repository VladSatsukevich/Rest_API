from django.contrib import admin
from . models import Message
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'date',)
    readonly_fields = ('id', 'name', 'text_of_problem', 'date',)
    list_filter = ('status',)
    search_fields = ('name',)


admin.site.register(Message, CategoryAdmin)
