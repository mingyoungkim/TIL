from django.urls import path
# 명시적 상대경로 표현
# .은 현재 디렉토리
# 지금 views랑 urls랑 같은 디렉토리에 있으니까
from . import views

app_name = 'articles'

urlpatterns = [
    # name의 value값은 웬만하면 view함수와 맞춰주기
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),

    # variable routing
    # 주소의 꺽쇠부분이 변수가 된 것 => 이 값을 마음대로 바꿀 수 있다.
    # <type:변수명> => type 의 기본값 str
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    # 각각의 특정글로 보내기
    # 고유값인 id를 기준으로 특정 글인 것을 명시
]
