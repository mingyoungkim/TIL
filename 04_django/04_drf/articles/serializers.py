# 이 페이지는 fomrs.py 와 동일하지만 분리해서 사용하는 것이 좋다
# rest_framework: drf 설치해서 사용할 수 있다
from rest_framework import serializers
from .models import Article, Comment

# modelform과 같은 구조
# comment는 어차피 content하나만 보여주니까 Serializer하나만 정의
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        # 조회시에만 article 컬럼 보여주기 (읽기전용)
        # 즉, 모든 컬럼 보여줄건데 article은 조회시에만 보여줌
        read_only_fields = ('article',)
        # 깊이 더 들어가서 article정보 보여줌
        depth = 1

class ArticleListSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(
            source='comments.count',
            read_only=True
        )


    class Meta:
        model = Article
        # 이때는 id, title만 보여주는 거니까 read_only 아님!!
        fields = ('id', 'title', 'comment_count',)

class ArticleSerializer(serializers.ModelSerializer):
    # 이 게시글이 어떤 댓글과 연결되어 있는지 보여주기 위한 필드???
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # 댓글들의 상세 내용까지 알고 싶다면 밑에꺼 쓰기 (위에는 comment의 pk만 받아옴)
    # CommentSerializer불러오기 위해 CommentSerializer 클래스를 위로 옮겨주기
    comment_set = CommentSerializer(many=True, read_only=True)
    # 역참조 field명인 comment_set을 바꾸고자 한다면,
    # model에서 related_name을 설정하고
    # 그이름 설정하면 됨

    # 댓글의 총 개수 나타내기
    # ORM으로 생각해보자. 특정 게시글이 가지고 있는 모든 댓글 개수
    # article = get_objects_or_404(Article, pk=1)
    # article.comment_set.count()
    comment_count = serializers.IntegerField(
        # source = 새로 추가할 field를 어떤 정보로 채울 것이냐?
        # comment_set.count로 채울 것이다 == article.comment_set.count()
        source='comment_set.count',
        # 읽기 전용이다. (생성, 수정 시 사용자가 데이터를 직접 입력하지 않는다.)
        read_only=True
        )
    
    class Meta:
        model = Article
        fields = '__all__'

       