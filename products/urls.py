from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^products/', views.home, name="home"),
    url('', views.home, name="home"),
    
]