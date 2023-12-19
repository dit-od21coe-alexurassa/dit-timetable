from django.views import generic
from django.http import HttpResponse
from django.forms.models import BaseModelForm
from django.urls import reverse_lazy

from ..forms import SessionForm
from ..models import Session
from ..utils import get_timetable


class SessionAddView(generic.CreateView):
    """Allows adding of a session to a specific visited timetable item. Timetable `pk` must be supplied in the url
    via `timetable_pk` kwarg
    """

    form_class = SessionForm

    def get_queryset(self):
        return Session.objects.filter(timetable__exact=get_timetable(view=self))

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        instance = form.save(commit=False)
        timetable = get_timetable(view=self)
        if timetable:
            instance.timetable = timetable
            instance.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy(
            "university:timetables:detail",
            kwargs={"timetable_pk": self.kwargs.get("timetable_pk")},
        )
