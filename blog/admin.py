from django.contrib import admin
from blog.models import Post

# Register your models here.


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['author', 'title', 'text', 'status', 'create_date']
    list_filter = ['author', 'title', 'status']
    search_fields = ['title', 'text']
    prepopulated_fields = {
        'slug': ('title',)
    }
    ordering = ['-status', '-create_date']