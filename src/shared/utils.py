from typing import Any
from django.views.generic import ListView, CreateView


class ListCreateView(ListView, CreateView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.object = None