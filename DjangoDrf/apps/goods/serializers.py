# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\10\20 0020 13:38$'

from rest_framework import serializers

from .models import Goods,GoodsCategory

#绑定models的数据
# class GoodsSerializers(serializers.Serializer):
#     name = serializers.CharField(required=True,max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()

#使用ModelSerializer绑定数据

#使得外键可以显示

#进行Serializer的嵌套使用。覆盖外键字段
class GoodsCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializers(serializers.ModelSerializer):
    category = GoodsCategorySerializers()   #进行Serializer的嵌套使用。覆盖外键字段
    class Meta:
        model = Goods
        fields = "__all__"
