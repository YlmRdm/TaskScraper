from django.conf.urls import url
from scraping import views 

urlpatterns = [ 
    url(r'^api/scraping$', views.scraping_list),
    url(r'^api/scraping/(?P<pid>[0-9]+)$', views.scraping_detail),
    url(r'^api/scraping/published$', views.scraping_list_published),
]