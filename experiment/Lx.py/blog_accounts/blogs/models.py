from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    title = models.CharField(max_length=500)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.title)>50:
            return f"{self.title[:50]}..."
        else:
            return self.title