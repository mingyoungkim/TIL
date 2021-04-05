from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    PasswordChangeForm,
)
from .forms import CustomUserChangeForm , CustomUserCreationForm


# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        # form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)

def profile(request, username):
    # Uer 모델에서 현재 user_id 가져오기
    # person이 없을 때 404오류 안뜨게 하기 위해서 get_object_or_404로 작성
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)

@require_POST
def follow(request, user_pk):
    # LIKE와 같이 user와 user의 관계를 정의 할 것이므로
    # 로그인 되어 있는지 먼저 확인
    if request.user.is_authenticated:
        # 내가 팔로 하려고 하는 대상
        you = get_object_or_404(get_user_model(), pk=user_pk)
        # 지금 팔로우 하려는 나
        me = request.user
        # 나는 나를 팔로우 불가
        if you != me:
            # 그런 내가 그사람의 팔로워들 안에 있으면 팔로우 끊음
            # if me in you.followers.all():
            # 이거보다
            # person의 follower들 중 내 pk가 같은 사람이 있는지 확인
            if you.followers.filter(pk=me.pk).exists(): # 왜 filter냐?? 없어도 오류나지 말라고!! (get은 쿼리셋을 주는 애가 아니라서 값이 없으면 오류남)
                # 팔로우 끊음
                you.followers.remove(me)
            else:
                # 팔로우 신청
                you.followers.add(me)
            # 프로필 페이지는 username 경로 필요
            return redirect('accounts:profile', you.username)
    # 로그인 안한 사용자 로그인페이지로
    return redirect('accounts:login')