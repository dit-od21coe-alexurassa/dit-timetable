from django.contrib import admin
from django.urls import re_path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path("^admin/", admin.site.urls),
    re_path("", include("university.urls.r_main", namespace="university")),
]

# media and static file url conf
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
