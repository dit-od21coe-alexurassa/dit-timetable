from django.urls import re_path

from ..views import *


app_name: str = "academic_years"

urlpatterns = [
    re_path(r"$", view=AcademicYearsListCreateView.as_view(), name="list"),
]
