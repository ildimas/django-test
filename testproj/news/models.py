from tabnanny import verbose
from unicodedata import category
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    content = models.TextField(blank=True, verbose_name='контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')
    we_are_fucked = models.BooleanField(default=True, verbose_name='Мы в дерьме ?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
    
        
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Наименование категории")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
    
        
        
