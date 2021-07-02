accounts앱 만들고 settings에 등록

base.html 만들기 => 경로 설정

User model정의

auth_user_model (setting에 등록)

migrations/migrate

admin으로 페이지 확인 (register => get_user_model)

---------------------------------------------------------------------------------

community app 만들기

urls.py에 등록

model 만들기 => review 모델 + comment모델

migrations/migrate

admin에 등록하고 잘 뜨는지 확인

index페이지 만들기

form 만들기 => meta에서 usre exclude해주기

create페이지만들기 

-------------------------------------------------------------------------

accounts앱의 crud 먼저!

login 먼저 만들기 (index 에서 로그인 하면 사용자 상태 알려주기)

nav바에 login 경로 넣기 (로그인 여부에 따라)

logout 만들기

회원가입 폼 커스텀

signup 만들고

--------------------------------------------------

community detail 만들기

CommentForm

댓글 생성 detail페이지 작업

--------------------------------------------------

community/forms.py

커스텀





## 댓글

model

form

detail페이지에 작성