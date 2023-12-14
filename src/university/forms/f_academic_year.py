from django import forms

from ..models import AcademicYear


class AcademicYearForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = AcademicYear
        fields = ['name']
        