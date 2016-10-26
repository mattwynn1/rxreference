from django.conf.urls import url
from . import views

urlpatterns = [    
    url(r'^search', views.Search),
    url(r'^(?P<code>[a-zA-Z0-9_.-]+)$', views.Drug),
    url(r'^', views.Main),
]
