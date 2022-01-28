from django.db import models

from profiles.models import UserProfile
from products.models import Product

class Feedback(models.Model):
    user_profile = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE,)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE,)
    date = models.DateField(auto_now_add=True)
    summary = models.CharField(max_length=250, null=False, blank=False)
    your_message = models.TextField(null=False, blank=False)
