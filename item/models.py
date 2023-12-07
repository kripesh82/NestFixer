from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    name=models.CharField(max_length=255)
    
    class Meta: 
        # category lai order ma rakhna 
        ordering = ('name',)

        # Spelling Milauna
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        # Cateogy lai afno naam dina lai
        return self.name

class Item(models.Model):
    Category=models.ForeignKey(category , related_name='items' , on_delete= models.CASCADE)
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True , null=True)
    price = models.FloatField()
    image=models.ImageField(upload_to='item_images' , blank=True, null=True)
    is_available = models.BooleanField(default=False)
    is_negotiable = models.BooleanField(default=False)
    location= models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='items' , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Item lai afno naam dina lai
        return self.name


