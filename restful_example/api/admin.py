from django.contrib import admin
from api.models import User,Token

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['name','user_type']

class TokenAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.register(User,UserAdmin)
admin.register(Token,TokenAdmin)