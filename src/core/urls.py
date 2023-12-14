from django.contrib import admin
from django.urls import re_path, include

urlpatterns = [
    re_path("^admin/", admin.site.urls),
    re_path("", include("university.urls.r_main", namespace="university")),
]
