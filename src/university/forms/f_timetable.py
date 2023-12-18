from shared.forms import StyledModelForm

from ..models import Timetable


class TimetableForm(StyledModelForm):
    class Meta:
        model = Timetable
        fields = ["academic_year", "semester"]
