from django.urls import re_path

from .views import *


app_name: str = "university"

urlpatterns = [
    re_path(r"timetables", view=TimetableTemplateView.as_view(), name="timetable"),
    re_path(r"academic-years", view=AcademicYearListCreateView.as_view(), name="academic_years")
]
