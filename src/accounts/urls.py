from django.urls import include, path
from rest_framework import routers
from . import views


# from .apps import AccountsConfig
#
# app_name = AccountsConfig.name


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
