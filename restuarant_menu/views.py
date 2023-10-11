from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


class MenuList(generic.ListView):
    model = Item
    queryset = Item.objects.order_by("-date_created")
    template_name = "index1.html"
    context_object_name = 'data_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['meals'] = Item.description
        return context


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
