from django.db import models

from profiles.models import UserProfile
from products.models import Product

class Feedback(models.Model):

    class Meta:
        verbose_name_plural = 'Feedback'

    user_profile = models.CharField(max_length=10, null=True, blank=True)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    summary = models.CharField(max_length=250, null=False, blank=False)
    your_message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.full_name
