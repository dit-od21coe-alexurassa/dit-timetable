from django.urls import re_path

from ..views import LecturersListCreateView, LecturerDetailUpdateView, LecturerDeleteView


app_name: str = "lecturers"


urlpatterns = [
    re_path(r"(?P<pk>\d+)/delete/$", LecturerDeleteView.as_view(), name="delete"),
    re_path(r"(?P<pk>\d+)/$", LecturerDetailUpdateView.as_view(), name="detail"),
    re_path(r"$", LecturersListCreateView.as_view(), name="list"),
]
