from shared.forms import StyledModelForm

from ..models import AcademicYear


class AcademicYearForm(StyledModelForm):

    class Meta:
        model = AcademicYear
        fields = ['name']
        