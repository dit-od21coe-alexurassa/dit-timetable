from typing import Any
from django.views import generic
from django.urls import reverse_lazy

from ..models import IntakeClass
from ..forms import IntakeClassForm


class IntakeClassesListCreateView(generic.ListView, generic.CreateView):

    template_name = "university/intake-classes.html"
    form_class = IntakeClassForm
    success_url = reverse_lazy("university:intake_classes")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return {
            "intake_classes": self.get_queryset(),
            "form": self.form_class
        }
    
    def get_queryset(self):
        return IntakeClass.objects.all()
