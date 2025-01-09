from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DeleteView

from apps.forms import OperatorModelForm
from apps.models import Operator


class HomeListView(ListView):
    queryset = Operator.objects.all()
    template_name = 'home_list.html'
    context_object_name = 'operators'

class HomeFormView(FormView):
    template_name = 'home.html'
    form_class = OperatorModelForm
    success_url = reverse_lazy('home-list')
    def form_valid(self, form):
         form.save()
         return super().form_valid(form)

def home_delete(request, pk):
    Operator.objects.filter(pk=pk).delete()
    return redirect('home-list')
