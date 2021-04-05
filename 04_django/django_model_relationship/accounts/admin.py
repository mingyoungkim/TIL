from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# admin에 사용자들 보여주기
# Register your models here.
admin.site.register(User, UserAdmin)