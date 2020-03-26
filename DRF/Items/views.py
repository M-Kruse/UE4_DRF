
from Items.models import Item
from django.views import generic
from django.shortcuts import get_object_or_404, render

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class ItemIndexView(generic.ListView):
    template_name = 'items/index.html'
    context_object_name = 'items_list'

    def get_queryset(self):
        return Item.objects.all()

class ItemDetailView(generic.DetailView):
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=kwargs['pk'])
        context = {'item': item}
        return render(request, 'items/item_detail.html', context)

class ItemsViewSet(viewsets.ModelViewSet):
    """
    View for in-game items.
    """
    queryset = Item.objects.all()
    # serializer_class = ItemSerializer
    # permission_classes = [permissions.IsAuthenticated]


