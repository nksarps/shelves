from .models import Bookshelf
from django.contrib import admin


class BookshelfAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Bookshelf, BookshelfAdmin)