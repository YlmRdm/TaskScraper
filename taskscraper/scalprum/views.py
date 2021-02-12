from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from scrapings.models import Scraping
from scrapings.serializers import ScrapingSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def scraping_list(request):
    if request.method == 'GET':
        scrapings = Scraping.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            scrapings = scrapings.filter(title__icontains=title)
        
        scrapings_serializer = ScrapingSerializer(scrapings, many=True)
        return JsonResponse(scrapings_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    # GET list of scrapings, POST a new scraping, DELETE all scrapings
    elif request.method == 'POST':
        scraping_data = JSONParser().parse(request)
        scraping_serializer = ScrapingSerializer(data=scraping_data)
        if scraping_serializer.is_valid():
            scraping_serializer.save()
            return JsonResponse(scraping_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(scraping_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Scraping.objects.all().delete()
        return JsonResponse({'message': '{} Scrapings were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def scraping_detail(request, pk):
    # ... scraping = Scraping.objects.get(pk=pk)
    if request.method == 'GET': 
        scraping_serializer = ScrapingSerializer(scraping) 
        return JsonResponse(scraping_serializer.data)
    elif request.method == 'PUT': 
        scraping_data = JSONParser().parse(request) 
        scraping_serializer = ScrapingSerializer(scraping, data=scraping_data) 
        if scraping_serializer.is_valid(): 
            scraping_serializer.save() 
            return JsonResponse(scraping_serializer.data) 
        return JsonResponse(scraping_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        scraping.delete() 
        return JsonResponse({'message': 'Scraping was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def scraping_list_published(request):
    scrapings = Scraping.objects.filter(published=True)
        
    if request.method == 'GET': 
        scrapings_serializer = ScrapingSerializer(scrapings, many=True)
        return JsonResponse(scrapings_serializer.data, safe=False)