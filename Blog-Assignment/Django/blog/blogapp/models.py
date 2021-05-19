from django.db import models

class Blog(models.Model): 
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self) -> str:
        return self.title

    def summary(self) -> str:
        return self.body[:100]
# Create your models here.
