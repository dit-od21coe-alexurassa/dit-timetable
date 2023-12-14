from typing import Any
from shared.forms import StyledModelForm

from ..models import IntakeStream


class IntakeStreamForm(StyledModelForm):
    class Meta:
        model = IntakeStream
        fields = ["class_code"]
