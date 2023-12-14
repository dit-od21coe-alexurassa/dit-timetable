from shared.forms import StyledModelForm

from ..models import Lecturer


class LecturerForm(StyledModelForm):

    class Meta:
        model = Lecturer
        fields = ['full_name', 'email', 'avatar']
        