from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Article # 현재 폴더의 models.py의 Article 클래스 가져오기
from .forms import ArticleForm # 현재 폴더의 forms.py의 ArticleForm 클래스 가져오기

# Create your views here.

# index페이지 같은경우 GET인 경우만 동작해야함
@require_safe
def index(request):
    # 받아온 쿼리셋을 최근생성한 게시물이 가장 위에 올라오도록 하자
    # 1. python 방식으로 해결하기
    # articles = Article.objects.all()[::-1]
    # 2. ORM사용해서 조작 => DB조작으로 내림차순으로 변경해서 쿼리셋 받기
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# create 같은 경우, GET, POST메서드만 기능 수행
@require_http_methods(['GET', 'POST'])
def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()    
    # 이렇게 말고 form을 이용하자

    # 내가 정의한 ArticleForm class 에
    # 사용자가 POST 방식으로 요청보낸 데이터와 함께
    # form instance 생성

    # POST일 때
    if request.method == 'POST':        
        form = ArticleForm(request.POST)
        if form.is_valid(): # 유효성 검사를 통과해서 True를 반환한다면, => 데이터가 있는지 or 글자 수 제한은 지켰는지 등등
            article = form.save() # 받아온 데이터 저장
            # render는 문서하나를 보여주는것 vs redirect는 url name으로 보내주는 것!
            return redirect('articles:detail', article.pk)   # 위에서 지정한 변수 article의 pk (pk는 글 생성되면 자동으로 생성됨)
    
    # GET일 때
    else:
        form = ArticleForm() # GET 방식때는 비어있는 input 태그 붙여주자
    # 사용자가 보낸 정보중에 유효한 정보들은 다시 담아서 new 페이지에 출력하고 입력안한 정보를 입력할 수 있도록 해줌
    # 여기는 두번째 if문을 통과하지 못했을 때, 내려오게 처리하기 위해 이런 생김새
    context = {
        # 상황에 따른 2가지 모습
        # 1. is_valid에서 내려온 form : 에러메세지를 포함한 form => 두번째 if문에서 통과못하고 내려온 경우
        # 2. else에서 내려온 form : 빈 form => 첫번째 if문에서 통과못하고 내려온 경우
        'form': form,
    }
    return render(request, 'articles/create.html', context)

@require_safe
def detail(request, pk):
    # article = Article.objects.get(pk=pk) => get 은 객체가 없거나 여러개일 경우, 에러발생
    # 그것을 방지하기 위해 get_object_or_404 이것을 import받아오고 쓰자
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # instance=article 가 없으면 create처럼 새로운 애가 생성됨
        # 수정을 하려고 하는 article을 데려오기 위해 사용
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        # 어떤 게시글인지 데려와서 원래 글의 정보를 가져오도록
        # 위에서 정의한 article 변수를 인스턴스인자로 가져옴 !!!!!!!!!!!!!!!!!!!
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        # form의 형태에서 정보를 뽑기 힘들어서 article 을 데려와서 정보 가져옴
        'article': article,
    }
    return render(request, 'articles/update.html', context)

# delete는 POST방식일때만, 삭제
# POST가 아니라면 HTTP ERROR 405에러메세지를 통해 method를 잘못보냈다고 알려줌
@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')