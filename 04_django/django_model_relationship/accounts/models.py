from django.db import models
from django.contrib.auth.models import AbstractUser
# 커스텀 유저 모델

# Create your models here.

# 정보를 다 갖추고 있어서 별도 수정은 필요없긴 함
class User(AbstractUser):
    pass