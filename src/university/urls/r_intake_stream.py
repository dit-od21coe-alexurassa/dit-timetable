from django.urls import re_path
from ..views import *

app_name: str = "streams"

urlpatterns = [
    re_path(
        r"(?P<stream_pk>\d+)/delete/$",
        view=IntakeStreamDeleteView.as_view(),
        name="delete",
    ),
    re_path(
        r"(?P<stream_pk>\d+)/$",
        view=IntakeStreamDetailUpdateView.as_view(),
        name="detail",
    ),
    re_path(r"$", view=IntakeStreamsListCreateView.as_view(), name="list"),
]
