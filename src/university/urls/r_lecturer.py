from django.urls import re_path

from ..views import LecturersListCreateView, LecturerDetailUpdateDelete


app_name: str = "lecturers"


urlpatterns = [
    re_path(r"(?P<pk>\d)/$", LecturerDetailUpdateDelete.as_view(), name="detail"),
    re_path(r"$", LecturersListCreateView.as_view(), name="list"),
]
