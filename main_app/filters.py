from django_filters import rest_framework as filter
from .models import event_table

class eventfilterset(filter.FilterSet):
    title = filter.CharFilter(field_name='title', lookup_expr='icontains')
    date = filter.DateFilter(field_name='date')
    category = filter.CharFilter(field_name='category__cat_name', lookup_expr='icontains')

    class Meta:
        model = event_table
        fields = ['title', 'date', 'category']