from django.urls import path

from . import views

app_name = "article"

urlpatterns = [
    path("", views.HomeView, name="home"),
    path("upload/", views.UploadImage.as_view(), name="upload-image")
]
