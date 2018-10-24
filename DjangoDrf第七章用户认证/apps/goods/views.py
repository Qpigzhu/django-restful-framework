# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination #分页
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .filters import GoodsFilter
from .models import Goods,GoodsCategory
from .serializers import GoodsSerializers,GoodsCategorySerializers

# Create your views here.

#APIView写的商品列表
# class GoodList(APIView):
#     """
#         GoodList 食品列表
#     """
#     def get(self,request,format=None):
#         #获取model的数据
#         goods= Goods.objects.all()[:10]
#         #创建serializers文件再绑定数据,一个数据的时候不需要加many=Ture
#         goods_serializer = GoodsSerializers(goods,many=True)
#         #返回Json格式
#         return Response(goods_serializer.data)




#定制分页的设置
class Goodspagination(PageNumberPagination):
    page_size = 12 #一页多少个数据的设定
    page_size_query_param = 'page_size' #可以动态获取一页多少个数据
    page_query_param = "page" #定制页数的属性值 列p=“2” 或 page = “2”
    max_page_size = 100 #最大获取一页多少个数据

"""
继承generics.ListAPIView写的商品列表页
"""
# class GoodsList(generics.ListAPIView):
#     """
#         GoodList 商品列表
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializers
#
#     #使得定制分页生效
#     pagination_class = Goodspagination

"""
继承viewsets写的商品列表页,使得有绑定URL更加便捷
"""
class GoodsList(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
        GoodList 商品列表,分页,过滤
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers

    #使得定制分页生效
    pagination_class = Goodspagination

    #设置三大常用过滤器之DjangoFilterBackend, SearchFilter查询过滤器,OrderingFilter排序过滤器
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    # 设置filter的类为我们自定义的类
    filter_class = GoodsFilter
    #查询过滤器
    search_fields = ('name', 'goods_brief', 'goods_desc')
    #排序过滤器
    ordering_fields = ('sold_num', 'shop_price')

    #微信认证配置
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (JSONWebTokenAuthentication,)


class CategoryViewset(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
        List：
            商品的分类列表
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class =GoodsCategorySerializers
