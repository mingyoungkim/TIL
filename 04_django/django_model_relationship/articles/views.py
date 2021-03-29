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
            article.user = request.user
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
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)

# @login_required # 로그인한 사람들만 댓글달기
# require_POST와 같이 못쓴느 이유는 @login_required 는 get과 post 두가지를 받을때 사용해주는 게 좋다. post만 받는 경우는 충돌 발생가능 그래서 is_authenticated로 밑에서 처리하는게 좋음
# GET일 때 따로 처리할 필요 없다 => detail 페이지가 처리하고 있기 때문! ????????????
@require_POST  
def comments_create(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        comment_form = CommentForm(request.POST) # request.POST 는 FORM으로부터 POST로 받은 사용자가 만든 데이터 # 이 변수도 그냥 form해도 되나?????????????????????????//
        if comment_form.is_valid():
            # commit=True(기본값)면 article_id 가 없어서 에러뜸
            # 인스턴스는 만들어주는데 데이터베이스에는 저장 안함 그러면 에러가 안뜸 => 추가적으로 데이터 작성할 시간을 줌
            comment = comment_form.save(commit=False)
            comment.article = article
            # comment.article_id = article.pk   
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
    # return HttpResponse(status=401)

@require_POST # POST일 때만 삭제
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)