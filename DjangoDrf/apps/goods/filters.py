# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\10\20 0020 17:00$'

from django_filters import rest_framework as filters
from goods.models import Goods


class GoodsFilter(filters.FilterSet):
    #name代表过滤的字段,lookup_expr代表过滤的条件,相当于Goods.objects.filter(shop_price__get=price_min)
    price_min = filters.NumberFilter(name='shop_price', lookup_expr='gte')
    price_max = filters.NumberFilter(name='shop_price', lookup_expr='lte')

    class Meta:
        model = Goods
        fields = ['price_min','price_max']
