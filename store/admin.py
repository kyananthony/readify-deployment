from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')  # Ensure 'email' is correctly spelled
    search_fields = ('name', 'email')       # Ensure 'email' is correctly spelled
    list_filter = ('name',)
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'bio')
        }),
    )
# Register your models here.
