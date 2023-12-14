from django import forms


class StyledModelForm(forms.ModelForm):
    """Renders a form with default styles"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class'] = 'form-control'