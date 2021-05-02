from django.db import models
from django.contrib.auth.models import AbstractUser
# 커스텀 유저 모델

# Create your models here.

# 정보를 다 갖추고 있어서 별도 수정은 필요없긴 함
class User(AbstractUser):
    # symmetrical=True 면 대칭 : 대칭이란, 팔로우하면 상대도 자동으로 맞팔 (인스타는 대칭 X)
    # symmetrical=False하면 related_name 지정해줌
    # => 상대방 입장에서의 역참조 manager 정의 해주기

    # ManyToManyField 는 다시 말하자면 !!
    #  기존 모델에 변경사항 X, 대신 중개테이블 생성
    
    # 일단 내 입장으로 followings
    # user - user의 관계이므로 self 써줌 (재귀참조)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')