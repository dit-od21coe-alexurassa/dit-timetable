from typing import Any
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
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


class LecturerDetailUpdateDelete(generic.UpdateView, generic.DetailView, generic.DeleteView):
    form_class = LecturerForm
    queryset = Lecturer.objects.all()
    template_name = "university/lecturer-detail.html"