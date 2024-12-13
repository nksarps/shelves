from .models import Book
from django.contrib import admin


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'isbn', 'author')
    readonly_fields = ('created_at',)


admin.site.register(Book, BookAdmin)