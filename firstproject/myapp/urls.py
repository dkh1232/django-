from django.urls import path, include
from . import views
urlpatterns = [
    path('index/yyds/',views.index),
    path('index/zfc/',views.zifuchuan),
    path('index/disange/',views.num3),
    path('index/', views.index1),
]
