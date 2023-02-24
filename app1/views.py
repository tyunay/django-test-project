from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Syndic, CarModel, CarModelSyndic, Property, Secretary
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import SortForm

def test(request):
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

    if request.method == 'POST':
        form = SortForm(request.POST)
        if form.is_valid():
            mylst = form.cleaned_data['input'].split(',')
            mylst2 = quicksort(mylst)
            return HttpResponse(quicksort(mylst2))
    else:
        form = SortForm()
    return render(request, 'sort.html', {'form': form})

class SyndicListView(ListView):
    model = Syndic
    template_name = 'syndics/syndic_list.html'

class SyndicDetailView(DetailView):
    model = Syndic
    template_name = 'syndics/syndic_detail.html'

class SyndicCreateView(CreateView):
    model = Syndic
    template_name = 'syndics/syndic_add.html'
    fields = ['surname', 'email','address','license_number','contact_number']

class SyndicUpdateView(UpdateView):
    model = Syndic
    template_name = 'syndics/syndic_update.html'
    fields = ['surname', 'email','address','license_number','contact_number']

class SyndicDeleteView(DeleteView):
    model = Syndic
    template_name = 'syndics/syndic_delete.html'
    success_url = reverse_lazy('syndic_list')

#####################################################

class SecretaryListView(ListView):
    model = Secretary
    template_name = 'secretaries/secretary_list.html'

class SecretaryDetailView(DetailView):
    model = Secretary
    template_name = 'secretaries/secretary_detail.html'

class SecretaryCreateView(CreateView):
    model = Secretary
    template_name = 'secretaries/secretary_add.html'
    fields = ['name', 'syndic']

class SecretaryUpdateView(UpdateView):
    model = Secretary
    template_name = 'secretaries/secretary_update.html'
    fields = ['name', 'syndic']

class SecretaryDeleteView(DeleteView):
    model = Secretary
    template_name = 'secretaries/secretary_delete.html'
    success_url = reverse_lazy('secretary_list')

#####################################################
class PropertyListView(ListView):
    model = Property
    template_name = 'properties/property_list.html'

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'properties/property_detail.html'

class PropertyCreateView(CreateView):
    model = Property
    template_name = 'properties/property_add.html'
    fields = ['identification_number', 'price','syndic','date_of_release']

class PropertyUpdateView(UpdateView):
    model = Property
    template_name = 'properties/property_update.html'
    fields = ['identification_number', 'price','syndic','date_of_release']

class PropertyDeleteView(DeleteView):
    model = Property
    template_name = 'properties/property_delete.html'
    success_url = reverse_lazy('property_list')
#####################################################
class CarModelListView(ListView):
    model = CarModel
    template_name = 'carmodels/carmodel_list.html'

class CarModelDetailView(DetailView):
    model = CarModel
    template_name = 'carmodels/carmodel_detail.html'

class CarModelCreateView(CreateView):
    model = CarModel
    template_name = 'carmodels/carmodel_add.html'
    fields = ['name']

class CarModelUpdateView(UpdateView):
    model = CarModel
    template_name = 'carmodels/carmodel_update.html'
    fields = ['name']

class CarModelDeleteView(DeleteView):
    model = CarModel
    template_name = 'carmodels/carmodel_delete.html'
    success_url = reverse_lazy('carmodel_list')
#####################################################
class CarModelSyndicListView(ListView):
    model = CarModelSyndic
    template_name = 'carmodelsyndics/carmodelsyndic_list.html'

class CarModelSyndicDetailView(DetailView):
    model = CarModelSyndic
    template_name = 'carmodelsyndics/carmodelsyndic_detail.html'

class CarModelSyndicCreateView(CreateView):
    model = CarModelSyndic
    template_name = 'carmodelsyndics/carmodelsyndic_add.html'
    fields = ['average_speed','car_model','syndic']

class CarModelSyndicUpdateView(UpdateView):
    model = CarModelSyndic
    template_name = 'carmodelsyndics/carmodelsyndic_update.html'
    fields = ['average_speed','car_model','syndic']

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['car_model'].label_from_instance = lambda obj: f"{obj.name}"
        form.fields['syndic'].label_from_instance = lambda obj: f"{obj.surname}"
        return form


class CarModelSyndicDeleteView(DeleteView):
    model = CarModelSyndic
    template_name = 'carmodelsyndics/carmodelsyndic_delete.html'
    success_url = reverse_lazy('carmodelsyndic_list')
