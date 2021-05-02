from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    # 글 삭제
    # 위의 경로와 구분하기위해 /delete/추가
    path('<int:pk>/delete/', views.delete, name='delete'),
    # 글 수정
    # 얘도 똑같이 특정 글을 수정해야함 (pk값 필요)
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
