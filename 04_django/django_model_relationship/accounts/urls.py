from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    # user의 프로필 페이지 구현 (이곳에 follow 표시해줄 거임)
    # 보통 프로필은 pk보다 user_id로 경로가 지정되는 경우가 많음
    # variable routing이 문자열로만 된 경우 위치 아래에 고정 필수 (현재 urlpatterns는 리스트라서 순차 검색)
    # 맨 위에 있게 되면 login/ logout이 username으로 알게됨
    path('<username>/', views.profile, name='profile'),
    # FOLLOW
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]