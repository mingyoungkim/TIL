from django.urls import path
from . import views

app_name = 'accounts'

# 로그인 기능 구현해보자
urlpatterns = [
    # 세션에 관한 create, delete
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # user에 관한 crud
    path('signup/', views.signup, name='signup'), # signup => user를 만든다(create)
    path('delete/', views.delete, name='delete'), # user를 삭제시킴(signout)
    path('update/', views.update, name='update'), # 회원정보 수정
    path('password/', views.change_password, name="change_password"),
]
