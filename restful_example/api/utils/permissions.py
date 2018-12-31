from rest_framework.permissions import BasePermission
from api.models import User,Token
class MyPermission(object):
    message = '无权访问'
    def has_permission(self,request,view):
        if request.user:
            return True     #如果不是匿名用户说明有权限
        else:
            return False    #否者无权限


class AdminPermission(object):
    message = '无权访问'
    def has_permission(self,request,view):
        if request.user == 'root':      # 管理员有权限
            return False
        return True

