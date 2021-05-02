from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            # user_id 라는 ForienKey를 받아와야 하니까 요청안에 user정보를 가져옴
            article.user = request.user # like_users 필드는?????????//
            article.save()                   
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # detail페이지에 댓글 보여주자
    comment_form = CommentForm()
    # django 내장 함수 (역참조 하는 경우에 comment 라는 매니저 를 사용)
    comments = article.comment_set.all() # article은 위에서 정의한 인스턴스 (특정 그 게시글의 모든댓글만 가져와야하니까)
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 게시글 작성자만 그 게시글 지울 수 있도록
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 게시글을 작성한 사람만 수정 가능하도록
    # 현재 요청되는 user 와 article의 user가 같으면 진행
    if request.user == article.user:    
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk) # 여기 그냥 pk 넣으면 안됨??? (comment_delete 처럼)
        else:
            form = ArticleForm(instance=article)
    # 현재 요청한 사용자가 작성자가 아니면 목록페이지로 보내줌
    else:
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)

# @login_required # 로그인한 사람들만 댓글달기
# require_POST와 같이 못쓰는 이유는 @login_required 는 get과 post 두가지를 받을때 사용해주는 게 좋다. post만 받는 경우는 충돌 발생가능 그래서 is_authenticated로 밑에서 처리하는게 좋음
# GET일 때 따로 처리할 필요 없다 => detail 페이지가 처리하고 있기 때문!
@require_POST  
def comments_create(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        comment_form = CommentForm(request.POST) # request.POST 는 FORM으로부터 POST로 받은 사용자가 만든 데이터
        if comment_form.is_valid():
            # commit=True(기본값)면 article_id 가 없어서 에러뜸
            # 인스턴스는 만들어주는데 데이터베이스에는 저장 안함 그러면 에러가 안뜸 => 추가적으로 데이터 작성할 시간을 줌
            comment = comment_form.save(commit=False)
            comment.article = article
            # comment.article_id = article.pk
            # 댓글 작성 user는 현재 요청하는 user가 됨
            comment.user = request.user
            comment.save() # 이제 데이터베이스에도 저장!!!
            return redirect('articles:detail', article.pk)
        context = {
            'comment_form': comment_form,
            'article': article,
        }
        # 유효성 검사를 통과 못해도 detail페이지 보여주자
        # 왜 redirect가 아니냐 ? => redirect는 유효성검사가 통과 못했다는 오류를 전달하지 못함
        return render(request, 'articles/detail.html', context)
    return redirect('accounts:login')
    # return HttpResponse(status=401) # 401 UNAUTHORIZED 반환

@require_POST # POST일 때만 삭제
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:  
        comment = get_object_or_404(Comment, pk=comment_pk)      
        # 지금 요청보낸 user와 댓글 작성한 user가 같을때만 삭제
        if request.user == comment.user:            
            comment.delete()
        # return HttpResponseForbidden() # 403 status code 반환
    return redirect('articles:detail', article_pk)
    # return HttpResponse(status=401)

# 데이터에 관여하는 행위기 때문에
@require_POST
def likes(request, article_pk):
    # 로그인한 사용자만 좋아요 누를 수 있도록
    # 현재 유저가 로그인 되어 있는지 => article과 user의 M:N 관계 설정을 하려면
    # 당연히 유저가 특정 PK값을 가진 생성되어 있는 유저여야 한다.
    if request.user.is_authenticated:
        # 특정 게시글에만 좋아요 추가 할 것
        article = get_object_or_404(Article, pk=article_pk)
        # 좋아요를 누른 user가 article의 좋아요를 누른 모든 user 리스트에 있으면 좋아요를 취소한다는 뜻
        # if request.user in article.like_users.all():
        # article에 연결된 pk가 현재 요청하는 user의 pk만 찾아서 적어도 하나 이상 존재하면 좋아요 했었다는 말
        # 이게 위의 if문보다 빠르니까 요걸로 쓰자 (모든 좋아요 누른 user를 조회하는 것보다 내 pk 찾는게 빠름)
        if article.like_user.filter(pk=request.user.pk).exists(): 
            # remove(), add() : 쿼리셋 AIP
            article.like_users.remove(request.user) # 좋아요 취소
        else:
            article.like_users.add(request.user) # article 관련 객체의 user객체를 추가 => 좋아요를 누른거임
        # redirect는 새로고침이 된다는 뜻 
        return redirect('articles:index')
    # 비로그인 사용자면 로그인페이지로
    return redirect('accounts:login')
