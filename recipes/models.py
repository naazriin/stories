from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(DateMixin):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
    

class Tags(DateMixin):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Tags'
        verbose_name = 'Tag'


class Reciepes(DateMixin):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')
    tags = models.ManyToManyField(Tags, related_name='recipes')
    authors = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Reciepes'
        verbose_name = 'Reciepe'

    def get_absolute_url(self):
        return reverse_lazy('recipe_single', kwargs={'slug': self.slug})

    def author_fullname(self):
        return f'{self.authors.username}'


class RecipeImages(models.Model):
    recipe = models.ForeignKey(Reciepes, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='recipes')

    def __str__(self):
        return f'{self.recipe.title} Image'

    class Meta:
        verbose_name_plural = 'RecipeImages'
        verbose_name = 'RecipeImage'


class Favorites(DateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    recipe = models.ForeignKey(Reciepes, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return f'{self.user.username} - {self.recipe.title}'
    
    class Meta:
        verbose_name_plural = 'Favorites'
        verbose_name = 'Favorite'
        ordering = ['-created_at']