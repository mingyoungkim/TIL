from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 이거는 왜하는 거지?????
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 댓글에 관한 모델
class Comment(models.Model):
    # 외래키의 변수명은 얘가 참조하는 모델의 소문자로 써줌
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # ForeignKey 필수 인자 2개 (참조하는애, on_delete) # 모델 참조가 왜필요 한거야 ? 둘 다
    content = models.CharField(max_length=200) # 댓글은 보통 길이제한 있으니까
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 댓글 구현할때 shell_plus사용할 거니까 출력할때 보기 쉽게
    def __str__(self):
        return self.content    
    
    # python manage.py shell_plus
    # Article.objects.create(title='제목1', content='내용1') => 게시글 먼저 만들어주고
    # comment = Comment()
    # comment.content = '댓글1'
    # comment.save()
    # article = Article.objects.get(pk=1) => article이라는 변수에 게시글1번 저장
    # comment.article = article => 처음 article은 class Comment에 만든 article, 뒤의 article은 바로 윗줄에서 만들 pk=1이 담긴 article
    # comment.save()

    # 역참조
    # article = Article.objects.get(pk=1)
    # article.comment_set.all()