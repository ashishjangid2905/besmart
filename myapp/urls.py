
from django.urls import path

from myapp import views


urlpatterns = [
    path('', views.index, name='home'),
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
    path('buyer/', views.buyer, name='buyer'),
    path('supplier/', views.supplier, name='supplier'),
    path('online/', views.online, name='online'),
    path('offline/', views.offline, name='offline'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('blogs/', views.blog, name='blog'),

]