from django.urls import reverse_lazy
from django.views import generic
from shared.utils import ListCreateView
from ..models import Lecturer
from ..forms import LecturerForm


class LecturersListCreateView(ListCreateView):
    template_name = "university/lecturers.html"
    form_class = LecturerForm
    success_url = reverse_lazy("university:lecturers:list")
    context_object_name = "lecturers"

    def get_queryset(self):
        return Lecturer.objects.all()


class LecturerDetailUpdateView(generic.UpdateView, generic.DetailView):
    form_class = LecturerForm
    queryset = Lecturer.objects.all()
    template_name = "university/lecturer_detail.html"


class LecturerDeleteView(generic.DeleteView):
    template_name = "university/lecturer_delete.html"
    queryset = Lecturer.objects.all()
    success_url = reverse_lazy("university:lecturers:list")
