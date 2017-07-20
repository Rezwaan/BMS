__author__ = 'Amad'
from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.getAll_Wearables, name="getAll_Wearables"),
    url(r'^sortASC$', views.getAll_WearablesASC, name="getAll_Wearables"),
    url(r'^sortDESC$', views.getAll_WearablesDESC, name="getAll_Wearables"),

    url(r'^getModels$', views.getAllWearablesModels, name="getAll_Wearables"),
    url(r'^filter/(?P<query>.+)/$', views.filterWearables, name="Filter"),
    url(r'^filterASC/(?P<query>.+)/$', views.filterWearablesASC, name="Filter"),
    url(r'^filterDESC/(?P<query>.+)/$', views.filterWearablesDESC, name="Filter"),

    url(r'^add/$',views.add_Wearables,name="add_Wearable"),

]