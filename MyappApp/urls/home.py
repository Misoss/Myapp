from django.conf.urls import url
#
from MyappApp.views.views import Home
#
urlpatterns_home = [
    url(r'', Home.as_view())
]
