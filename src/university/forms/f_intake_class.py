from shared.forms import StyledModelForm

from ..models import IntakeClass


class IntakeClassForm(StyledModelForm):
    class Meta:
        model = IntakeClass
        fields = ["academic_year", "class_code"]
