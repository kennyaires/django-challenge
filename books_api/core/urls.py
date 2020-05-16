from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls))
]