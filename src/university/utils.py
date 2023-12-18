from django.shortcuts import get_object_or_404
from .models import Timetable, IntakeStream


def get_stream(view, pk_url_kwarg: str = "stream_pk") -> IntakeStream:
    return get_object_or_404(IntakeStream, pk=view.kwargs.get(pk_url_kwarg))


def get_timetable(view, pk_url_kwarg: str = "timetable_pk") -> Timetable:
    return get_object_or_404(Timetable, pk=view.kwargs.get(pk_url_kwarg))
