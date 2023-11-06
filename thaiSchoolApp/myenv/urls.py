from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('thai_school_map',views.thaiSchoolMap, name='thaiSchoolMap'),
    path('getProvinceFromDB', views.getProvinceFromDB, name='getProvinceFromDB'),
    path('filterPoi', views.filterPoi, name='filterPoi'),
    path('detailPage',views.detailPage, name="detailPage"),
    path('testPage',views.testPage, name='testPage')
    # path('ConvertToGeoJsonList', views.ConvertToGeoJsonList, name='ConvertToGeoJsonList'),
    # path('testQueryKey', views.testQueryKey, name='testQueryKey')
]
