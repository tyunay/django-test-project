from django.urls import path
from .views import SyndicListView, SyndicDetailView, SyndicCreateView, SyndicUpdateView, SyndicDeleteView,SecretaryListView, SecretaryDetailView, SecretaryCreateView, SecretaryUpdateView, SecretaryDeleteView, PropertyListView, PropertyDetailView, PropertyCreateView, PropertyUpdateView, PropertyDeleteView, CarModelSyndicListView, CarModelSyndicDetailView, CarModelSyndicUpdateView, CarModelSyndicDeleteView, CarModelSyndicCreateView, CarModelListView, CarModelDetailView, CarModelCreateView, CarModelUpdateView, CarModelDeleteView
from django.views.generic import TemplateView
from . import views

urlpatterns = [
        path('test', views.test),
        path('', TemplateView.as_view(template_name = 'base.html')),

        path('syndics/', SyndicListView.as_view(), name = 'syndic_list'),
        path('syndics/<int:pk>', SyndicDetailView.as_view(), name='syndic_detail'),
        path('syndics/add', SyndicCreateView.as_view(), name='syndic_add'),
        path('syndics/update/<int:pk>', SyndicUpdateView.as_view(), name='syndic_update'),
        path('syndics/delete/<int:pk>', SyndicDeleteView.as_view(), name='syndic_delete'),

        path('secretaries/', SecretaryListView.as_view(), name='secretary_list'),
        path('secretaries/<int:pk>', SecretaryDetailView.as_view(), name='secretary_detail'),
        path('secretaries/add', SecretaryCreateView.as_view(), name='secretary_add'),
        path('secretaries/update/<int:pk>', SecretaryUpdateView.as_view(), name='secretary_update'),
        path('secretaries/delete/<int:pk>', SecretaryDeleteView.as_view(), name='secretary_delete'),

        path('properties/', PropertyListView.as_view(), name='property_list'),
        path('properties/<int:pk>', PropertyDetailView.as_view(), name='property_detail'),
        path('properties/add', PropertyCreateView.as_view(), name='property_add'),
        path('properties/update/<int:pk>', PropertyUpdateView.as_view(), name='property_update'),
        path('properties/delete/<int:pk>', PropertyDeleteView.as_view(), name='property_delete'),

        path('carmodels/', CarModelListView.as_view(), name='carmodel_list'),
        path('carmodels/<int:pk>', CarModelDetailView.as_view(), name='carmodel_detail'),
        path('carmodels/add', CarModelCreateView.as_view(), name='carmodel_add'),
        path('carmodels/update/<int:pk>', CarModelUpdateView.as_view(), name='carmodel_update'),
        path('carmodels/delete/<int:pk>', CarModelDeleteView.as_view(), name='carmodel_delete'),

        path('carmodelsyndics/', CarModelSyndicListView.as_view(), name = 'carmodelsyndic_list'),
        path('carmodelsyndics/<int:pk>', CarModelSyndicDetailView.as_view(), name = 'carmodelsyndic_detail'),
        path('carmodelsyndics/add', CarModelSyndicCreateView.as_view(), name = 'carmodelsyndic_add'),
        path('carmodelsyndics/update/<int:pk>', CarModelSyndicUpdateView.as_view(), name = 'carmodelsyndic_update'),
        path('carmodelsyndics/delete/<int:pk>', CarModelSyndicDeleteView.as_view(), name = 'carmodelsyndic_delete'),
        ]
