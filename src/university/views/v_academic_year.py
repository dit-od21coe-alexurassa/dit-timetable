from typing import Any
from django.views import generic
from django.urls import reverse_lazy

from ..models import AcademicYear
from ..forms import AcademicYearForm


class AcademicYearListCreateView(generic.ListView, generic.CreateView):

    template_name = "university/academic_years.html"
    form_class = AcademicYearForm
    success_url = reverse_lazy("university:academic_years")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return {
            "academic_years": self.get_queryset(),
            "form": self.form_class
        }
    
    def get_queryset(self):
        return AcademicYear.objects.all()
