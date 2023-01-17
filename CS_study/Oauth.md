# OAuth 2.0
 > 사용자가 비밀번호를 제공 않고 타 웹사이트나 어플에 접근 권한(`Access Token`)을 부여해 해당 정보를 사용하도록 하는 프로토콜
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

## 인증종류
  - 권한부여승인 (Authorization Code Grant)
     - 권한 부여 승인을 위해 자체 생성한 Authorization Code를 전달하는 방식
     - 가장 많이 쓰이는 기본적인 방식
     - 간편 로그인 기능에서 사용되는 방식
     - 클라이언트가 사용자를 대신하여 특정 자원에 접근을 요청할 때 사용
     - Refresh Token 사용 가능한 방식
  - 암시적 승인 (Implicit Grant)
     - 권한 부여 코드 승인 타입과 다르게 권한 코드 교환 단계 없이 엑세스 토큰을 즉시 반환받아 이를 인증에 이용하는 방식
       (인증 코드 빼고 모두 동일한 과정)
  - 클라이언트 자격 증명 승인 (Client Credentials Grant)
     - 클라이언트가 컨텍스트 외부에서 액세스 토큰을 얻어 특정 리소스에 접근을 요청할 때 사용
  - 리소스 소유자 암호 자격 증명 승인 (Resource Owner Password Credentials Grant)
     - 클라이언트가 암호를 사용하여 엑세스 토큰에 대한 사용자의 자격 증명을 교환


## 참고링크
  1. OAuth 이용해 인증 구현
     - https://velog.io/@devjade/OAuth-authentication-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0github-%EB%A1%9C%EA%B7%B8%EC%9D%B8

  2. OAuth 모듈 구현
     - https://cozy-ho.github.io/server/2021/07/19/Nodejs%EB%A1%9C-OAuth-%EC%9D%B8%EC%A6%9D%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0-oidc-provider.html
     - java로 구현 !!!! : https://co-de.tistory.com/29

## Kakao 로그인 구현
  > 권한부여승인 인증종류 사용
  
  - ID와 비밀번호로 사용자 신원을 확인
  - 로그인 세션 대신 사용 가능한 ID 토큰 제공 
  - 액세스 토큰(Access token), 리프레시 토큰(Refresh token) 두 종류의 토큰을 발급

  ### 토큰
     - Access token
       : 사용자 인증, API 호출 권한 부여
         (Android, iOS : 12시간, JavaScript: 2 시간, REST API : 6시간)
      => 카카오계정 세션
        클라이언트에서 사용자가 이미 카카오계정으로 로그인한 상태라면 카카오계정 세션이 존재
        로그인 시 카카오계정 세션의 인증 시간은 기본 `24시간`
        사용자가 카카오계정 로그인 화면에서 [로그인 상태 유지]를 선택한 경우에는 인증 시간이 `1달`입니다.
     - Refresh token
       : 액세스 토큰 재발급에 사용
         유효한 리프레시 토큰이 있다면 사용자가 매번 카카오계정 정보를 입력하거나 로그인하는 인증 절차를 거치지 않아도 액세스 토큰 재발급 가능
         (how????)
         (2달, 만료 시간 1달 남은 시점부터 갱신 가능)
     - ID token
       : 로그인 사용자의 인증 정보를 제공하는 토큰
         (만료시간은 액세스 토큰과 동일)
    => Kakao SDK는 토큰 관리 기능 내장, REST API 사용 시 필요에 따라 토큰 정보 확인하기 또는 토큰 갱신하기 요청 필요

  ### OpenID Connect 지원
     - 사용자 인증 정보를 담은 ID 토큰을 함께 발급
