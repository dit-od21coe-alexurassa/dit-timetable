from django.urls import re_path, include

from ..views import *


app_name: str = "intake_classes"

urlpatterns = [
        re_path(r"(?P<class_pk>\d)/streams/", include("university.urls.r_intake_stream", namespace="streams")),
        re_path(r"$", view=IntakeClassesListCreateView.as_view(), name="list"),
        re_path(r"(?P<class_pk>\d)/", view=IntakeClassDetailUpdateDeleteView.as_view(), name="detail"),
]
