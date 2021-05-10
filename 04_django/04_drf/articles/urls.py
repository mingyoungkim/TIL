from django.urls import path
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
    #   description="Test description",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
    #   license=openapi.License(name="BSD License"),
   ),
)

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    # 댓글이 생성될때 특정게시글의 댓글인 것을 
    path('articles/<int:article_pk>/comments/', views.comments_create),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    # path('comments/<int:comment_pk>/', views.comment_create), => 바로 위의 경로에 먹어서 detail경로가됨
    path('swagger/', schema_view.with_ui('swagger')),
]
