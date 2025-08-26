from django.db import models
from account.models import CustomUser

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    
    is_premium = models.BooleanField(default=False, verbose_name="Is this a premum article?")
    
    user = models.ForeignKey(CustomUser, max_length=10, on_delete=models.CASCADE, null=True)