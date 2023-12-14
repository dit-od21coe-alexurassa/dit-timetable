from django.urls import reverse_lazy
from django.views import generic
from shared.utils import ListCreateView
from ..models import Module
from ..forms import ModuleForm


class ModulesListCreateView(ListCreateView):

    template_name = "university/modules.html"
    form_class = ModuleForm
    success_url = reverse_lazy("university:modules:list")
    context_object_name = "modules"

    
    def get_queryset(self):
        return Module.objects.all()


class ModuleDetailUpdateDelete(generic.UpdateView, generic.DetailView, generic.DeleteView):
    form_class = ModuleForm
    queryset = Module.objects.all()
    template_name = "university/module-detail.html"