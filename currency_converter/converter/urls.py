from django.urls import path
from .views import ConvertView


urlpatterns = [
    path("converter", ConvertView.as_view()),
]
