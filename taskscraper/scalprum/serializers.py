from rest_framework import serializers 
from scraping.models import Scraping

class ScrapingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scraping
        fields = (
            'pid',
            'title',
            'images',
            'productCategory',
            'colors',
            'prices',
            'discount'
            )