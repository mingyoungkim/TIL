from django import forms
from .models import Article

# <ModelForm>
class ArticleForm(forms.ModelForm):
    # 각 필드마다 위젯을 정의
    title = forms.CharField(
        # label, widget, error_messages => form필드에서 사용하고 있는 built-in keyword 인자들임
        label='제목',
        # TextInput => 길이제한 있을때 넣어줌
        widget=forms.TextInput(
            # 속성을 attributes라는 dict형태로 넣어주기
            attrs={
                'class': 'title-input',
            }
        ),
        # 에러메세지 내용 수정
        error_messages={
            # 만약 required를 지키지 않았다면 => form을 만들때 자동으로 정의되는 required
            # 공백을 넣은 경우, '값을 입력해 주세요'가 위에 작성됨
            'required': '값을 입력해 주세요'
        }
    )

    class Meta:
        # 어떤 모델에 대한 정보 저장
        # 등록의 개념이라서 Article()의 형태인 호출의 개념이 아님 => 괄호 주의!!!!
        model = Article
        # 어떤 필드에 대한 정보 저장
        # Article이 가진 모든 필드를 불러오자 (title, content,,)
        fields = '__all__'
        # fields = ('title', 'content') 처럼 일일이 넣어도 됨

# => 단 세줄에 model에 정의한 Article 클래스 사용

#############################################################################
# # <Form>
# # Article model에 대한 Form이여서
# class ArticleForm(forms.Form):
#     # list 보통 대문자로 정의
#     # pjt의 settings의 형식과 갇다
#     REGIONS = [
#         # 실제 데이터 값, html에 렌더링 될 문자열
#         ('gumi', '구미'),
#         ('seoul', '서울'),
#         ('gwangju', '광주'),
#         ('daejeon', '대전'),
#     ]

#     # model에 정의한 컬럼들에 대한 내용들 넣어줌
#     title = forms.CharField(max_length=10)
#     # TextField없음
#     content = forms.CharField(
#         # 없어서 input태그 였던 것을 textarea로 바꿔줌
#         widget=forms.Textarea(
#             attrs={'class': 'special'}
#         )
#     )

#     # radio를 만들기 위해 select option 쓰는 것을 줄여줌
#     # ChoiceField 에는 리스트 인자 받아줌 (위에서 정의해주고 받아오기)
#     region = forms.ChoiceField(
#         choices=REGIONS, 
#         widget=forms.RadioSelect
#     )
