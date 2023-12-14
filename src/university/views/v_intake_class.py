from typing import Any
from django.views import generic
from django.urls import reverse_lazy

from ..models import IntakeClass
from ..forms import IntakeClassForm


class IntakeClassesListCreateView(generic.ListView, generic.CreateView):
    template_name = "university/intake-classes.html"
    form_class = IntakeClassForm
    success_url = reverse_lazy("university:intake_classes:list")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return {"intake_classes": self.get_queryset(), "form": self.form_class}

    def get_queryset(self):
        return IntakeClass.objects.all()


class IntakeClassDetailUpdateDeleteView(
    generic.DetailView, generic.UpdateView, generic.DeleteView
):
    template_name = "university/intake-class-detail.html"
    form_class = IntakeClassForm
    context_object_name = "intake_class"
    pk_url_kwarg = "class_pk"
    queryset = IntakeClass.objects.all()

    # def get_context_data(self, **kwargs) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context["streams"] =
    #     return context
