from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    # 댓글 내용 : form으로 받기 & 몇번 글 : url로 받기
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    # 댓글 삭제 => 댓글 pk도 가져와야함
    # 경로 설정 때, 깔끔하고 규칙성있게 만들어준다
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]
