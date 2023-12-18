from django.urls import re_path

from ..views import SessionAddView


app_name: str = "sessions"


urlpatterns = [re_path(r"add/$", view=SessionAddView.as_view(), name="add")]
