from django.http import HttpResponse
# django 의 http 규약에 관한 곳에서 HttpResponse(응답과 관련된 클래스??? 가져오기)
# 댓글 못다는 사람들 401페이지로 오류 보내서 로그인부터하도록
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
# AuthenticationForm 로그인 폼에 사용되는 것 가져오는 거 (로그인을 하기위한 폼)
# UserCreationForm 회원가입을 하기 위한 폼
# UserChangeForm 회원정보 수정
# PasswordChangeForm 일반 유저들의 비밀번호 변경해주는 폼 => 이것 역시 ModelForm이 아니라서 두번째 인자에 reqeust.user로 데이터받아야함
# django의 contribute의 auth(인증과 관련된) fomrs에서 가져옴

# user관련 form은 model form

from .forms import CustomUserChangeForm

from django.contrib.auth.decorators import login_required
# 'login한 경우만' 이라는 조건 데코레이터

from django.contrib.auth import login as auth_login 
# 지금 def login과 내장함수 login()이 같으니까 login()을 auth_login()으로 바꿔주자
# def login을 바꿔주지 않는 이유는 좀 더 직관적으로 주소와 일치시키기 위해
from django.contrib.auth import logout as auth_logout # 상동

from django.contrib.auth import update_session_auth_hash

# Create your views here.

# 로그인도 세션을 create하는 것임
# 게시글을 create하는 것과 동일
# 그러므로 mothod를 GET, POST에 대한 조건
# GET => 로그인 문서 보내줌
# POST => 로그인 진행
@require_http_methods(['GET', 'POST'])
def login(request):
    # 이미 로그인을 한 사용자는 이 로그인 페이지가 보여지면 안됨
    if request.user.is_authenticated: # 속성이기 때문에 ()로 호출하지 않음
        return redirect('articles:index')
    if request.method == 'POST':
        # AuthenticationForm (ModelForm이 아니라 Form임)
        # 첫번째인자로 request받고 데이터 받음 => Form 이니까
        # form = AuthenticationForm(request, data=request.POST)
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 여기는 저장이 아니라 세션을 create하는 거임 => 그 함수가 login()이라는 내장 함수
            # login() 함수는 request와 User 두 개의 인자를 받음
            auth_login(request, form.get_user())
            # request.GET.get('next') => next라는 키 받으면 next=/ parameter가 받아지게 하기
            # login_required 데코레이터로 로그인 안한 사용자가 url로 create 페이지 접근하면 주소가 next=/ 라는 parameter가 따라옴
            # 그 후, 로그인 성공하면 next=/ parameter가 받아지게 하기
            # 그러면 next=/articles/index
            return redirect(request.GET.get('next') or 'articles:index') # or은 앞이 참이면 뒤는 신경 안씀
    # django는 내장된 인증에 대한 form이 존재 => Authentication Form => built-in Form 가져오자
    # 내장 Form을 사용하기 때문에 forms.py 안만들어도 됨
    else:
        form = AuthenticationForm() 
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

# delete와 같은 형식
@require_POST
def logout(request):
    if request.user.is_authenticated: # 로그인한 사용자만 로그아웃가능
        auth_logout(request) # 얘는 요청인자가 하나 들어감 => 요청에 관한 세션 데이터와 그것과 연결되어 있는 db의 세션 데이터 삭제함
    return redirect('articles:index')

@require_http_methods(['GET', 'POST'])
def signup(request):
    # 이미 로그인한 사용자는 signup url로도 들어올 수 없음
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        # UserCreationForm
        # 얘는 ModelForm => 데이터가 먼저 인자로 받아져야함
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # 게시글을 저장하는 것 처럼 user를 저장 (save() 해서 user가 return 이 됐음)           
            auth_login(request, user) # 회원가입하면 바로 로그인 상태로 만들어주기
            return redirect('articles:index')
    else:
        form = UserCreationForm() # GET method인 경우 회원가입을 하는 빈 폼 가져오기
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@require_POST
def delete(request):
    if request.user.is_authenticated:        
        request.user.delete() # user 지움
        auth_logout(request) # 사용자 삭제하고 로그아웃해서 세션에 있는 정보까지 지우기
    return redirect('articles:index')

@login_required # 로그인 안한 사용자가 이 페이지 보려고 했을 때 로그인 페이지로 돌아가게됨 (대신 next=/ => parameter 돌려줌)
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        # 지금 user정보가 request에 담겨있음
        form = CustomUserChangeForm(request.POST, instance=request.user) # 현재 요청에 들어온 user를 수정해야하니까 instance로 넣어줌
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # form = UserChangeForm() => form.py에 커스텀해주자
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

@login_required # 로그인때만 접근해야하므로
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # form.save()
            # save() 는 비밀번호 변경하면 로그인이 풀림 why? => session값이 달라져서 session_id가 사라져버림 (db에 있던 session도 사라짐)
            # 비밀번호 변경하면 다시 로그인하면 새로운 session_id 생기면서 로그인 상태가 됨
            user = form.save()
            update_session_auth_hash(request, form.user) # 이거 왜 user 아니냐고오오오옹오오오!!!!!!!!!!!!!!!           
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)