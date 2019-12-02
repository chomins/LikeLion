from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=200)
    writer=models.CharField(max_length=200)
    date= models.DateTimeField('date published')
    body=models.TextField()

    def __str__(self):
        return self.name

    def __str__(self):
        return self.writer

    def summary(self):
        return self.body[:100]