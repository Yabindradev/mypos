from django.urls import path
from .import views

app_name =" pos"

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('setting', views.setting, name='setting'),
    
    
]