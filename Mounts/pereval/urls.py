from django.urls import path, include
from .views import MountViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mount', MountViewSet, basename='mount')

urlpatterns = [
    path('submitData/', include(router.urls)),
]


