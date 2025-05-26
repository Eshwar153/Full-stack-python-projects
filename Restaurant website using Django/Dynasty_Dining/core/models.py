from django.db import models
from django.utils import timezone


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 stars
    comments = models.TextField()

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name} - {self.rating}⭐"
    

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking for {self.name} on {self.date} at {self.time}"

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    card_holder = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment by {self.card_holder} for booking #{self.booking.id}"


class FoodOrder(models.Model):
    dish_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=8, decimal_places=2)
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dish_name} × {self.quantity}"
    


class CouponSubmission(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    coupon_code = models.CharField(max_length=50)
    offer_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name} - {self.coupon_code}"
#Create your models here.
