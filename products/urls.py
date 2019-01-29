from django.conf.urls import url, include
from . import views
urlpatterns = [


    url('', views.home, name="home"),
    #url('', views.home, name="home"),
    #url(r'^$', 'products.views.home', name='home'),
    url(r'^all/', views.all, name='all'),

  ]