from shared.forms import StyledModelForm

from ..models import Session


class SessionForm(StyledModelForm):
    class Meta:
        model = Session
        exclude = ["timetable"]
