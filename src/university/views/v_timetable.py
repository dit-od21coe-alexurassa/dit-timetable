from typing import Any
from django.forms.models import BaseModelForm
from django.views import generic
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from general.models import WeekDay
from ..models import *
from ..forms import TimetableForm, SessionForm
from ..utils import get_stream

class CreateTimetableView(generic.CreateView):
    template_name = "university/timetable/add_timetable.html"
    form_class = TimetableForm
    queryset = Timetable.objects.all()

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        instance: Timetable = form.save(commit=False)
        instance.intake_stream = get_stream(view=self)
        instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        stream = get_stream(view=self)
        return reverse_lazy(
            "university:intake_classes:streams:detail",
            kwargs={"class_pk": stream.intake_class.pk, "stream_pk": stream.pk},
        )

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["stream"] = get_stream(view=self)
        return context


class StreamTimetablesListView(generic.ListView):
    template_name = "university/stream_timetables.html"

    def get_queryset(self):
        return Timetable.objects.filter(intake_stream__exact=get_stream(view=self))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stream"] = get_stream(view=self)
        return context


class TimetableDetailUpdateView(generic.UpdateView, generic.DetailView):
    form_class = TimetableForm
    template_name = "university/timetable/timetable_detail.html"
    pk_url_kwarg = "timetable_pk"
    queryset = Timetable.objects.all()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["sessions"] = self.get_sessions()
        context["week_days"] = WeekDay.objects.all()
        context["session_form"] = SessionForm
        return context

    def get_sessions(self):
        return Session.objects.filter(timetable__exact=self.get_object())


class AcademicYearSelectionView(generic.ListView):
    template_name = "university/timetable/academic_year_selection.html"

    def get_queryset(self):
        return AcademicYear.objects.all()


class IntakeClassSelectionView(generic.ListView):
    template_name = "university/timetable/intake_class_selection.html"

    def get_queryset(self):
        return IntakeClass.objects.filter(academic_year=self.get_academic_year())

    def get_academic_year(self) -> AcademicYear or Http404:
        return get_object_or_404(AcademicYear, pk__exact=self.kwargs.get("acyear_pk"))


class IntakeStreamSelectionView(generic.ListView):
    template_name = "university/timetable/stream_selection.html"

    def get_queryset(self):
        return IntakeStream.objects.filter(intake_class__exact=self.get_intake_class())

    def get_intake_class(self) -> IntakeClass or Http404:
        return get_object_or_404(IntakeClass, pk__exact=self.kwargs.get("class_pk"))


class StreamTimetableView(generic.ListView):
    template_name = "university/timetable/stream_timetable.html"

    def get_queryset(self):
        return Timetable.objects.filter(intake_stream__exact=get_stream(view=self))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["week_days"] = WeekDay.objects.all()
        context["sessions"] = self.get_sessions()
        return context

    def get_sessions(self):
        sessions = Session.objects.filter(timetable__in=self.get_queryset())
        return sessions
