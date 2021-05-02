from django.db import models

# Create your models here.

# model은 객체지향언어니까 객체인 class 사용
# 어떤 model을 작성하던 django에 있는 models라는 모듈에 있는 Model 클래스를 가져온다
class Article(models.Model):
    # 컬럼 만들어주기
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 둘 다 텍스트 type인데 필드이름 다른 이유
    # CharField : 보통 제목의 길이를 제한 두니까 길이의 제한이 있는 텍스트 형태인 아이를 사용 (필수인자인 max_length필요)
    # TextField : 길이의 제한이 없을 때 사용

    created_at = models.DateTimeField(auto_now_add=True) # 생성될 때만 add되니까 auto_now_add 로 외우쟝
    updated_at = models.DateTimeField(auto_now=True)            