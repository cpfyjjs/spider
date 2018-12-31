import re

from rest_framework import serializers
from api.models import User,Movie
from api.models import MovieDetail,Category,Person


class PasswordValidator(object):
    def __init__(self,regx):
        self.regx = regx

    def __call__(self, value):
        if re.fullmatch(self.regx,value):
            msg = '密码不符合规则'
            raise serializers.ValidationError(msg)

    def set_context(self,serializer_field):
        """
            This hook is called by the serializer instance,
            prior to the validation call being made.
            """
        # 执行验证之前调用,serializer_fields是当前字段对象
        pass




# class UserSerizlizer(serializers.Serializer):
#     name = serializers.CharField(min_length=2,error_messages={'require':'姓名不能为空'})
#     password = serializers.CharField(min_length=6,validators=[PasswordValidator('cui.*')],
#                                      error_messages={'require':'密码不能为空',
#                                                      'min_length':'最小长度为2'},)
#     user_type = serializers.IntegerField(default=1)

# 用户序列化
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['name','password','user_type']
        # depth =2
        extra_kwargs = {
            'user':{'min_length':3},
            'password':{'min_length':6,'validators':[PasswordValidator('cui.*')]},
        }
        # read_only_fields = ['user']


# 电影序列化
class MoviesSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2)
    date = serializers.CharField(min_length=4, max_length=4)
    location = serializers.CharField(min_length=2)
    directors = serializers.CharField(min_length=2)

# 电影详情序列化
class MovieDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        field = "__all__"