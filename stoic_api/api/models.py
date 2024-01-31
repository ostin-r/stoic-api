from django.db import models


class Quote(models.Model):
    quote = models.CharField(max_length=1024)
    author = models.CharField(max_length=100)
    source = models.ForeignKey('Source', on_delete=models.PROTECT, null=True, blank=True)
    is_daily = models.BooleanField()

class Source(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')    
    isbn = models.CharField(max_length=13)

class Author(models.Model):
    name = models.CharField(max_length=100)

