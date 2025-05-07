from django.contrib import admin

from blog.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ['title', 'main_content', 'slug','img']
    list_display = ["title", "main_content", 'slug', 'created_at', "img"]
    prepopulated_fields = {'slug': ('title',)}
    model = Blog