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
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='items' , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Item lai afno naam dina lai
        return self.name


 

class Comment(models.Model):
    item = models.ForeignKey('Item', related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    item = models.ForeignKey('Item', related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 scale
    created_at = models.DateTimeField(auto_now_add=True)
