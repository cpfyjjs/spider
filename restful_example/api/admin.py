from django.contrib import admin
from api.models import User,Token,Movie

from api.models import MovieDetail,Person,Category

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['name','user_type']


class TokenAdmin(admin.ModelAdmin):
    list_display = ['user']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name','date','location','directors']
    list_filter = ['date']
    list_per_page = 10


class MovieDetailAdmin(admin.ModelAdmin):
    list_display = ['name','date','language','category']
    list_filter = ['date']

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(User,UserAdmin)
admin.site.register(Token,TokenAdmin)
admin.site.register(MovieDetail,MovieDetailAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(Category,CategoryAdmin)
