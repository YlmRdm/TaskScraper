from django.db import models

class Scraping(models.Model):
    pid = models.CharField(max_length=70, blank=False, default='')
    title = models.CharField(max_length=70, blank=False, default='')
    images = models.CharField(max_length=70, blank=False, default='')
    productCategory = models.CharField(max_length=70, blank=False, default='')
    colors = models.CharField(max_length=70, blank=False, default='')
    prices = models.CharField(max_length=70, blank=False, default='')
    discount = models.BooleanField(default=False)
    # description = models.CharField(max_length=200,blank=False, default='')