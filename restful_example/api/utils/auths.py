# _*_coding:utf-8_*_
# 用于认证和授权
from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication

from api.models import User,Token

class LoginAuth(BaseAuthentication):
    def authenticate(self, request):
        """
        用户认证，如果用户认证成功返回元祖：（用户，用户TOKEN)
        :param request:
        :return:
            None：表示跳过认证；
                如果跳过了所有认证，默认用户和Token和使用配置文件进行设置
                self._authenticator = None
                if api_settings.UNAUTHENTICATED_USER:
                    self.user = api_settings.UNAUTHENTICATED_USER() # 默认值为：匿名用户
                else:
                    self.user = None

                if api_settings.UNAUTHENTICATED_TOKEN:
                    self.auth = api_settings.UNAUTHENTICATED_TOKEN()# 默认值为：None
                else:
                    self.auth = None
            (user,token)表示验证通过并设置用户名和TOKEN(request.user = user,request.auth = token)
            AuthenticationFailed异常
        """
        token = request._request.COOKIES.get('token')
        if not token:
            return None

        token_obj = Token.objects.filter(token=token).first()
        if not token_obj:
            return None
        user = token_obj.user
        return user,token


    def authenticate_header(self, request):
        # 验证失败时，返回的响应头WWW-Authenticate对应的值
        pass
