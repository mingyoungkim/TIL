# Project Review_Jenkins 활용법

## why CI/CD?

- 워터폴 프로세스에서는 딜리버리가 `one time`

- 애자일 프로세스에서는 `many times`

  - 매 스프린트마다 딜리버리 하려면

    요구사항 분석 -> 설계 -> 개발 -> QA

  - 일의 양이 상당함

  - 이에 대한 부담을 줄이려면 자동화가 필수

    => **CI/CD의 탄생**

- 도구들

  - Travis CI
  - CircleCI
  - Jenkins
  - 등등~



## Jenkins

> 정의

- Java로 작성된 자동화 서버 -> os를 타지 않는 장점!
- MIT Licence
  - 변형만 없으면 잘 쓰임
  - 확장성이 좋다
- 다양한 플러그인을 사용해 CI/CD 파이프라인을 만들어 자동화 작업을 완성



### 설치

1. 베어 인스톨

   - 인스톨러를 사용해 PC나 서버에 설치

   - JRE 8, 11 만 지원

2. 컨테이너

   - `docker pull jenkins/jenkins:lts`
   - 컨테이너에 JRE가 포함
   - docker 컨테이너에 대한 이해 필요

3. 

