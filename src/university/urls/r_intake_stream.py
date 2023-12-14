from django.urls import re_path
from ..views import *

app_name: str = "streams"

urlpatterns = [
    re_path(r"$", view=IntakeStreamsListCreateView.as_view(), name="list"),
]
