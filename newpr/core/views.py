from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Product
from django.views import View
from django.views.generic import ListView, DetailView
from .filters import ProductFilter

class ProductListView(ListView):
    model = Product
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'index.html'
