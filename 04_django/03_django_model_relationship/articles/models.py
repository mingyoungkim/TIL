from django.db import models
from django.conf import settings

class Article(models.Model):
    # user와 article의 1:N
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # LIKE => user와 article의 M:N (중개 테이블 자동 생성) => 중개테이블 명 : '앱이름_모델이름_필드이름'
    # 반드시 복수를 만들 필요는 없지만, 복수의 유적와 관계 되므로 보통 복수형으로 작성
    # related_name => 동일한 이름의 manager가 생성되는 상황을 막기 위해,
    # MTM related_name (역참조 시 매니저명) 을 생성
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 댓글에 관한 모델
class Comment(models.Model):
    # article 과 comment의 1:N
    # 외래키의 변수명은 얘가 참조하는 모델의 소문자로 써줌
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # ForeignKey 필수 인자 2개 (참조하는애, on_delete)
    # user와 comment의 1:N
    # 외래키 하나 더 작성해주기 (사용자별 보이게)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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