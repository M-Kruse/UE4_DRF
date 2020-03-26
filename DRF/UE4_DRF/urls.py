
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('items/', include('Items.urls')),
    path('api/', include('api.urls')),
]