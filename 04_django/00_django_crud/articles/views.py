from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    # 받아온 쿼리셋을 최근생성한 게시물이 가장 위에 올라오도록 하자
    # 1. python 방식으로 해결하기
    # posts = Post.objects.all()[::-1]
    # 2. ORM사용해서 조작 => DB조작으로 내림차순으로 변경해서 쿼리셋 받기
    posts = Post.objects.order_by('-pk')
    context = {
        'posts': posts,
    }
    return render(request, 'articles/index.html', context)

# 새 글을 만들기 위한 페이지일뿐
# def new(request):
#     return render(request, 'articles/new.html')

# 새 글을 만드는 행위를 정의한 함수
def create(request):
    # 일단 만들때, if문으로 분개하기 전, render해서 창 보여주고 확인
    if request.method == 'POST':

        title = request.POST.get('title')
        content = request.POST.get('content')

        # Post.objects.create(title=title, content=content)
        # 조금 더 직관적으로 만들어주자
        post = Post(title=title, content=content)
        post.save()
        # 이제는 detail페이지로 이동해보자!!!
        # render는 문서하나를 보여주는것 vs redirect는 url name으로 보내주는 것!
        return redirect('articles:detail', post.pk)
    else:
        return render(request, 'articles/form.html')

def detail(request, pk):
    # post = Post.objects.get(pk=pk) => pk값이 없으면 오류가 뜨게됨
    # 그것을 방지하기 위해 get_object_or_404 이것을 import받아오고 쓰자
    post = get_object_or_404(Post, pk=pk)

    context = {
        'post': post,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':        
        post.delete()
        return redirect('articles:index')
    return redirect('articles:detail', post.pk)

# def edit(request, pk):
#     # post = Post.objects.get(pk=pk)
#     post = get_object_or_404(Post, pk=pk)
#     context = {
#         'post': post,
#     }
#     # 수정된 화면을 넘겨받아햐 하니까 render
#     return render(request, 'articles/edit.html', context)

def update(request, pk):
    if request.method == 'POST':
        # post = Post.objects.get(pk=pk)
        post = get_object_or_404(Post, pk=pk)

        title = request.POST.get('title')
        content = request.POST.get('content')

        post.title = title
        post.content = content
        post.save()
        return redirect('articles:detail', post.pk)
    else:
        context = {
            'post': post,
        }
        return render('articles/form.html', context)

