from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookList

router = DefaultRouter()
router.register(r'Book', BookList)

urlpatterns=[
        path('api/', include(router.urls)),
        ]
