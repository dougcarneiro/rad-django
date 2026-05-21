from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AutorViewSet, EditoraViewSet


router = SimpleRouter()
router.register(r'autor', AutorViewSet, basename='autor')
router.register(r'editora', EditoraViewSet, basename='editora')


urlpatterns = [
    path('', include(router.urls)),
]