from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

#App namespace
app_name = 'api'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'items', views.ItemViewSet, 'items')
router.register(r'heartbeat', views.HeartbeatViewSet, 'heartbeat')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]