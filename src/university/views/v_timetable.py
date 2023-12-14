from django.views.generic import ListView

from ..models import *


class TimetableTemplateView(ListView):
    template_name = "university/timetable.html"
    context_object_name = "timetables"

    def get_queryset(self):
        return Timetable.objects.all()
