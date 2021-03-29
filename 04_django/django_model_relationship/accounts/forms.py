from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)

# 재정의
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # UserCreationForm안에 Meta안에 있는 field값 쓸거임 + (User field에 있는 것)
        fields = UserCreationForm.Meta.fields + ('email',)