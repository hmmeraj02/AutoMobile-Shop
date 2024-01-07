from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User
# Create your models here.
class Car(models.Model):
    model_name = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='car/media/uploads/')
    buyer = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.model_name

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self.name}"