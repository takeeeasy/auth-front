"""auth_service2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from ts25_auth import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/find', views.find_user),
]


# from django.contrib import admin
# from django.urls import path
# from rest_framework import routers
# from ts25_auth.views import UserViewSet
# from django.conf.urls import url, include
#
#
# router = routers.DefaultRouter()
# router.register('userId', UserViewSet)
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^', include(router.urls)),
# ]
