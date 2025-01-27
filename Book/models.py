from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    author = models.CharField(max_length=50, default='anonymous')
    email = models.EmailField(blank=True)
    describe = models.TextField(default='I love Django.')

    def __str__(self):
        return self.name
    