# OAuth 2.0
 > 사용자가 비밀번호를 제공 않고 타 웹사이트나 어플에 접근 권한을 부여해 해당 정보를 사용하도록 하는 프로토콜
   (1.0에서 보안문제 개선한 버전)
   [!프로토콜이란?](./%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C.md)

## OAuth 참여자
  - Resource Server : Client가 제어하고자 하는 자원을 보유하고 있는 서버
    (Facebook, Google, Twitter 등)
  - Resource Owner : 자원의 소유자
    (Client가 제공하는 서비스를 통해 로그인하는 실제 유저)
  - Client : Resoure Server에 접속해서 정보를 가져오고자 하는 클라이언트(웹 어플리케이션)

## OAuth Flow
  https://tecoble.techcourse.co.kr/post/2021-07-10-understanding-oauth/
  [!Oauth2.0_process](./README_images/oauth2.0-process.png)
  => 셍활코딩 OAuth 

## 생활코딩
  - 정보를 제공하는 웹사이트의 아이디와 비밀번호를 제공하지 않고 `Access Token`을 부여해 발급
  - 즉, 필수적 기능만 사용하도록 함
  - 참여자
