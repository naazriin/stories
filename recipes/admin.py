from django.contrib import admin
from django.utils.html import format_html 
from modeltranslation.admin import TranslationAdmin

from .models import Category, Tags, Reciepes, RecipeImages, Favorites

admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(RecipeImages)
admin.site.register(Favorites)


class RecipeImagesInline(admin.TabularInline):
    model = RecipeImages
    extra = 2


class RecipeAdmin(TranslationAdmin):
    list_display = ['id', 'title','slug', 'get_image', 'get_tags', 'category', 'authors', 'created_at', 'updated_at', 'is_active']
    list_display_links = ['id', 'title', 'created_at']
    list_editable = ['category', 'authors', 'is_active']
    list_filter = ['category', 'tags']
    inlines = [RecipeImagesInline]

    fieldsets = [
        ('Recipe Info', {'fields': ['title', 'description', 'image', 'slug']}),
        ('Relations', {'fields': ['category', 'tags', 'authors']})
    ]

    def get_image(self, obj):
        if obj.image:
            image = f"<img src='{obj.image.url}' style='width: 100px; height: 100px;' />"
            return format_html(image)
        return 'No Image'
    
    get_image.short_description = 'Image'
    
    def get_tags(self, obj):
        return ', '.join([tag.name for tag in obj.tags.all()])
    
    get_tags.short_description = 'Tags'



admin.site.register(Reciepes, RecipeAdmin)
