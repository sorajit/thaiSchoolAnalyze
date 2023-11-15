from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('getProvinceFromDB', views.getProvinceFromDB, name='getProvinceFromDB'),
    path('filterPoi', views.filterPoi, name='filterPoi'),
    path('detailPage',views.detailPage, name="detailPage")
]
