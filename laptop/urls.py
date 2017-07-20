from django.conf.urls import url

from .  import views

urlpatterns = [

    url(r'^$',views.getAll_Laptops,name="getAll_Laptops"),
    url(r'^sortASC$', views.getAllLaptopsSortASC, name="getAll_Laptops"),
url(r'^sortDESC$', views.getAllLaptopsSortDESC, name="getAll_Laptops"),

    url(r'^add/$',views.add_Laptop,name="add_Laptop"),
    url(r'^delete/$',views.delete,name="add_Laptop"),

    url(r'^getModels$',views.getModels,name="Models"),

    url(r'^filterlaptop/(?P<query>.+)/$', views.FilterLaptops,name="Filter"),

    url(r'^filterlaptopASC/(?P<query>.+)/$', views.FilterLaptopsAsc, name="Filter"),
    url(r'^filterlaptopDESC/(?P<query>.+)/$', views.FilterLaptopsDesc, name="Filter"),

]