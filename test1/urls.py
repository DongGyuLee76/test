from django.urls import path
from . import views_1

urlpatterns = [
    path('',views_1.index,name='index'),
]