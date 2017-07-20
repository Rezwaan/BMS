__author__ = 'Amad'
from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$',  views.index, name='index'),
    url(r'^viewAll$',views.getAll_Mobiles,name="getAll_Mobiles"),
    url(r'^viewAllASC$', views.getAll_MobilesASC, name="getAll_Mobiles"),
    url(r'^viewAllDESC$', views.getAll_MobilesDESC, name="getAll_Mobiles"),

    url(r'^AddMobile$',views.add_Mobiles,name="Add Mobiles"),

    url(r'^getModels$',views.getModels,name="Models"),
    url(r'^filtermobile/(?P<query>.+)/$', views.Filter_Mobiles,name="Filter"),
    url(r'^filtermobileASC/(?P<query>.+)/$', views.Filter_MobilesASC, name="Filter"),
    url(r'^filtermobileDESC/(?P<query>.+)/$', views.Filter_MobilesDESC, name="Filter"),

]