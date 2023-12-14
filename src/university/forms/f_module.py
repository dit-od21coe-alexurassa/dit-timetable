from shared.forms import StyledModelForm

from ..models import Module


class ModuleForm(StyledModelForm):

    class Meta:
        model = Module
        fields = ['title', 'code']
        