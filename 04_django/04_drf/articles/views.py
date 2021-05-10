from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# get_list_or_404 는 조회 페이지에 게시글이나 댓글 암것도 없을때 오류 알려줌
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
# post 요청에 입력할 body를 ArticleSerializer를 기준으로 shcema 생성
@swagger_auto_schema(methods=['POST'], request_body=ArticleSerializer)
@api_view(['GET', 'POST'])
def article_list(request):
    # GET, POST방식 페이지 완전히 다름 (각 방식 페이지 보이는 것 다름)
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        # many: 단일객체냐 아니냐 (현재는 queryset이니까 단일객체 아니니까 many=True로 설정)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data) # serializer.data을 넘겨줄때 dict 형태로 넘겨준다
    elif request.method == 'POST':
        # 사용자가 넘겨준 데이터
        serializer = ArticleSerializer(data=request.data)
        # 유효성 검사 및 예외처리
        if serializer.is_valid(raise_exception=True):
            # 게시글 생성(저장)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # serializer.errors: 오류뜰때 어떤 부분에 오류뜨는지 알려줌
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) => 유효성검사에 옵션 raise_exception=True 넣으면 필요 X

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':        
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        # 삭제했을때, 좀 더 친절하게 표기 (삭제되었다고 내용 보여주기)
        data = {
            'id': article_pk,
            'delete': f'data {article_pk} is deleted!!'
        }
        # 삭제되서 내용 없다는 상태
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        # 글 수정할 때는 특정 게시글에 관한 정보도 가져와야함
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view기본값 GET (일단 적어는 주자)
@api_view(['GET'])
def comment_list(request):
    # 모든 댓글 불러오기
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # 특정 댓글을 사용자가 보내준 데이터로 수정
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            # article에 대한 정보 필요없다 (댓글 수정으로 참조중인 article이 변동되는 일은 없기때문)
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        # 삭제는 serializer 무관하게 해당 comment 삭제하면 됨
        comment.delete()
        data = {
            'id': comment_pk,
            'delete': f'data {comment_pk} is deleted!!',
        }
        # 삭제를 밑에 두고 데이터에 .pk로 받아서 표현도 가능
        # data = {
        #     'id': comment.pk,
        #     'delete': f'data {comment.pk} is deleted!!',
        # }
        # comment.delete()
        return Response(data, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def comments_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 사용자가 입력한 데이터 (content) 넣어주고
    serializer = CommentSerializer(data=request.data)
    # 유효성검사와 예외처리
    # 이때 article 필드도 같이 검사해서 article이라는 정보 안넣어주면 유효 성검사 통과못해서 400오류뜸 => read_only_fields 필요
    if serializer.is_valid(raise_exception=True):
        # article 정보 넣어주는거 serializer 자체에 article=article 이렇게 하면 추가 정보 담아줄 수 있음
        serializer.save(article=article)
        # 그래서 아래의 과정 안해도 됨
        # serializer = serializer.save(commit=False)
        # serializer.article = article
        # serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)