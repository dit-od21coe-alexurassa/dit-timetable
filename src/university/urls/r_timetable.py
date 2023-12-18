from django.urls import re_path, include

from ..views import *


app_name: str = "timetables"

urlpatterns = [
    re_path(
        r"year-selection/",
        view=AcademicYearSelectionView.as_view(),
        name="year_selection",
    ),
    re_path(
        r"intake-selection/(?P<acyear_pk>\d+)/",
        view=IntakeClassSelectionView.as_view(),
        name="intake_selection",
    ),
    re_path(
        r"stream-selection/(?P<class_pk>\d+)/",
        view=IntakeStreamSelectionView.as_view(),
        name="stream_selection",
    ),
    re_path(
        r"stream/(?P<stream_pk>\d+)/add",
        view=CreateTimetableView.as_view(),
        name="add_timetable",
    ),
    re_path(
        r"stream/(?P<stream_pk>\d+)/list",
        view=StreamTimetablesListView.as_view(),
        name="list",
    ),
    re_path(
        r"stream/(?P<stream_pk>\d+)/",
        view=StreamTimetableView.as_view(),
        name="stream_timetable",
    ),
    re_path(
        r"(?P<timetable_pk>\d+)/sessions/",
        include("university.urls.r_session", namespace="sessions"),
    ),
    re_path(
        r"(?P<timetable_pk>\d+)/",
        view=TimetableDetailUpdateView.as_view(),
        name="detail",
    ),
]
