import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from api.models import User,Token,Movie
from api.utils.base import BaseResponse
from uuid import uuid4
# Create your views here.
from api.utils import permissions,auths,serialize


class LogView(APIView):
    authentication_classes = []
    permission_classes = []

    # def get(self,request):
    #     print('开始创建数据')
    #     with open('D:\spider\dygang\movie.txt', mode='r') as f:
    #         for r in f.readlines():
    #             try:
    #                 if len(r) > 200:
    #                     continue
    #                 movies = json.loads(r, encoding='utf-8')
    #                 name = movies.get('name')
    #                 date = movies.get('age')
    #                 location = movies.get('location')
    #                 directors = movies.get('director')
    #                 Movie.objects.create(name=name,date=date,location=location,directors=directors)
    #                 print(movies)
    #             except:
    #                 pass
    #     base = BaseResponse()
    #     return Response(base.dict)


    def post(self,request):
        name = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(name=name).first():
            return Response(BaseResponse(status=100,msg='fail').dict)
        user = User.objects.create(name=name,password=password)
        uuid = uuid4()
        Token.objects.create(user=user,token=uuid)
        result = Response(BaseResponse().dict)
        result.set_cookie('token',uuid)
        return result


    def patch(self,request):
        base = BaseResponse()
        name = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(name=name).first():
            return Response(base.dict)
        base.status = 100
        base.msg = 'fail'
        return Response(base.dict)



class MovieView(APIView):
    #authentication_classes = [auths.LoginAuth]
    #permission_classes = [permissions.MyPermission]

    def get(self,request):
        movie = Movie.objects.all()
        ser = serialize.MoviesSerializer(instance=movie,many=True)

        return Response(ser.data)

    def permission_denied(self, request, message=None):
        if request.authenticators and not request.successful_authenticator:
            raise exceptions.NotAuthenticated('嘿嘿')
        raise exceptions.PermissionDenied(detail=message)

