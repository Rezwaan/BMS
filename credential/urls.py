__author__ = 'Amad'
from django.conf.urls import url,include
#from django.views.decorators.csrf import csrf_exempt
from rest_framework_jwt.views import obtain_jwt_token
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    url(r'^users/$', views.user_list, name='user_list'),
    url(r'^email/$', views.emailToFriend, name='email'),

    url(r'^usersDetails/$', views.userDetaillist, name='userDetailslist'),
    url(r'^user-token-auth/', obtain_jwt_token),
    url(r'^getID/(?P<query>.+)/$', views.getID, name="Filter")

]
urlpatterns = format_suffix_patterns(urlpatterns)