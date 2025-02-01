from django.urls import path
from . import views

app_name = 'travel'

urlpatterns = [
    path('', views.home, name='home'),
    path('map/', views.map_view, name='map'),
    path('destination/<str:city>/', views.destination_detail, name='destination_detail'),
    path('comment/<str:city>/', views.add_comment, name='add_comment'),
]