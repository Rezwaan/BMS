from django.conf.urls import url

from . import APIS

urlpatterns = [

    url(r'^suggestions/(?P<query>.+)/$',APIS.AutoComplete ,name="Search Result"),


    url(r'^filter/(?P<query>.+)/$',APIS.FilterLaptops ,name="Search Result"),
    url(r'^filterDESC/(?P<query>.+)/$', APIS.FilterLaptopsDESC, name="Search Result"),
    url(r'^filterASC/(?P<query>.+)/$', APIS.FilterLaptopsASC, name="Search Result"),

    url(r'^filterbyModelASC/(?P<query>.+)/$', APIS.FilterLaptopsbyModelUPCASC, name="Search Result"),
    url(r'^filterbyModelDESC/(?P<query>.+)/$', APIS.FilterLaptopsbyModelUPCDESC, name="Search Result"),
    url(r'^filterbyModel/(?P<query>.+)/$', APIS.FilterLaptopsbyModelUPC, name="Search Result"),

    url(r'^filtergroupon/(?P<query>.+)/$', APIS.FilterGroupon, name="Search Result"),
    url(r'^filtergrouponASC/(?P<query>.+)/$', APIS.FilterGrouponASC, name="Search Result"),
    url(r'^filtergrouponDESC/(?P<query>.+)/$', APIS.FilterGrouponDESC, name="Search Result"),

    url(r'^count$', APIS.CountAll, name="Count Result"),
    url(r'^countQuery/(?P<query>.+)/$', APIS.CountQueryAll, name="Search Result"),

]