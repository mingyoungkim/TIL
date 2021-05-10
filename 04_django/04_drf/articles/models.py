from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # 댓글이 참조하고 있는 Article
    # Article이 삭제 되면 댓글도 같이 삭제 => on_delete
    # article_comment 테이블에는
    # article_id 라고 하는 컬럼이 생성
    # 특정 comment는 article을 .natation을 통해 직접 참조 가능
    # 반면, 특정 article의 입장에서는 역참조 매니저 comment_set을 통해 접근!
    # 역참조 매니저 이름은 related_name 옵션을 통해 바꿀 수 있다 (보통 N:N 관계에서)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)