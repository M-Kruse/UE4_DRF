from django.urls import path
from django.contrib.auth.decorators import login_required

from Items import views

app_name = "items"

urlpatterns = [
    path(
        '',
        views.ItemIndexView.as_view(),
        name="detail"
    ),
    path(
        'detail/<int:pk>',
        login_required(views.ItemDetailView.as_view()),
        name="detail"
    ),
]