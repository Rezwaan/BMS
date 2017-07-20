from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from subjects import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^subjects/', views.subjectslist.as_view(), name='hsn'),
    #url(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view())
    #url(r'^subjects/(?P<filename>[^/]+)$', views.subjectslist.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)