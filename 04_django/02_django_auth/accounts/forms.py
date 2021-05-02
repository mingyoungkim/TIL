from django.contrib.auth.forms import UserChangeForm
# django가 가지고있는 user로 부터 
# UserChangeForm 이라는 built-in Form 이 슈퍼유저가 사용하는 Form으로 구성되어 있기 때문에
# 커스텀해줄 필요가 있다.
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm): # 상속을 받아서 출력되는 필드만 조정할 거임

    # ModelForm의 정보 저장하는 곳
    class Meta: # UserChangeForm 얘가 ModelForm임
        model = get_user_model() # get_user_model() 함수임!! => User모델 안데꼬오고 얘를 델고옴 (활성화되어있는 User Model)
        fields = ('email', 'first_name', 'last_name',) # django 문서의 user object에 field 참조