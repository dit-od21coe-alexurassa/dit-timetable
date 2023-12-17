from typing import Any
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from shared.utils import ListCreateView

from ..models import IntakeStream, IntakeClass
from ..forms import IntakeStreamForm


class IntakeStreamsListCreateView(ListCreateView):
    """Return streams that belong to a particular `IntakeClass`"""

    template_name = "university/intake-streams.html"
    form_class = IntakeStreamForm
    context_object_name = "intake_streams"

    def get_queryset(self):
        return IntakeStream.objects.filter(intake_class__exact=self.get_intake_class())

    def get_success_url(self):
        return reverse_lazy(
            "university:intake_classes:streams:list",
            kwargs={"class_pk": self.get_intake_class().pk},
        )

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["intake_class"] = self.get_intake_class()
        return context

    def get_intake_class(self) -> IntakeClass or Http404:
        return get_object_or_404(IntakeClass, pk__exact=self.kwargs.get("class_pk"))

    def form_valid(self, form):
        stream: IntakeStream = form.save(commit=False)
        stream.intake_class = self.get_intake_class()
        stream.save()
        return super().form_valid(form)


class IntakeStreamDetailUpdateView(generic.DetailView, generic.UpdateView):
    template_name = "university/intake_stream_detail.html"
    form_class = IntakeStreamForm
    pk_url_kwarg = "stream_pk"
    queryset = IntakeStream.objects.all()
    context_object_name = "stream"


class IntakeStreamDeleteView(generic.DeleteView):
    template_name = "university/intake_stream_delete.html"
    pk_url_kwarg = "stream_pk"
    queryset = IntakeStream.objects.all()
    context_object_name = "stream"

    def get_success_url(self):
        return reverse_lazy(
            "university:intake_classes:streams:list",
            kwargs={"class_pk": self.get_object().intake_class.pk},
        )
