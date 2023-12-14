from django.urls import re_path

from ..views import ModulesListCreateView, ModuleDetailUpdateDelete


app_name: str = 'modules'


urlpatterns = [
    re_path(r"(?P<pk>\d)/$", ModuleDetailUpdateDelete.as_view(), name="detail"),
    re_path(r"$", ModulesListCreateView.as_view(), name="list"),
]
