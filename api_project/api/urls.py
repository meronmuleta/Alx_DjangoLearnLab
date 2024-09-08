from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'Book', BookViewSet)

urlpatterns=[
        path('api/', include(router.urls)),
        ]
