from django.urls import path 
from . import views

urlpatterns = [
    path('api/titles', views.TitleList.as_view(), name='title_list'),
    path('api/titles/<int:pk>', views.TitleDetail.as_view(), name='title_detail'),
]