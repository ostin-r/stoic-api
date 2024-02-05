from django.db import models


class Quote(models.Model):
    quote = models.CharField(max_length=1024)
    author = models.CharField(max_length=100)
    source = models.ForeignKey('Source', on_delete=models.PROTECT)
    is_daily = models.BooleanField(default=False)

class Source(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')    
    isbn = models.CharField(max_length=13)

class Author(models.Model):
    name = models.CharField(max_length=100)

