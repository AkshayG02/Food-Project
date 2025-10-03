from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=25)
    category = models.CharField(max_length=30)
    price = models.FloatField()
    img = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.food.price

    def __str__(self):
        return f"{self.quantity} x {self.food.name} - {self.user.username}"


    def get_absolute_url(self):
        return "/list"



# class Contact(models.Model):
#     name= models.CharField(max_length=25)
#     Contact=models.IntegerField()
#     email= models.EmailField()



