from django.db import models
from django.conf import settings
Users = settings.AUTH_USER_MODEL


class Article(models.Model):
    content = models.TextField(null=True, blank=False)
    image = models.ImageField(upload_to="images")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
