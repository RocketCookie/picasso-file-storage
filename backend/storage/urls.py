from django.urls import path

from storage.views import files, upload

file_urlpatterns = [
    path("upload/", upload, name="upload"),
    path("files/", files, name="files"),
]
