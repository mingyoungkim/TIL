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

## Build
 > 서버에 올릴 수 있는 상태로 만드는 것
 - 서버에 반영을 하는 것 : `배포`
 - 배포 하기 위한 준비 과정 : `빌드`

## Jenkins
 > build 를 자동으로 해주는 툴

- Java로 작성된 자동화 서버 -> os를 타지 않는 장점!
- MIT Licence
  - 변형만 없으면 잘 쓰임
  - 확장성이 좋다
- 다양한 플러그인을 사용해 CI/CD 파이프라인을 만들어 자동화 작업을 완성

 🤔 Why? 자동화?
 - 간편화 자동화로 시간 단축
 - 예전) 자바를 빌드 할 때 javac라는 커맨드를 직접 사용 
   지금은 IDEA를 이용하면 main()메소드를 실행했을 때 javac를 하고 java가 실행
   => 이렇게 반복되는 작업을 자동화

 ### 대표적인 기능
   1. 대쉬보드 제공 : 여러가지 배포 작업의 상황을 모니터링 
   2. 배포 스크립트 실행기능 : 배포 스크립트를 개발자 로컬에서도 실행 할 수 있는데 젠킨스라는 프로그램을 띄워놓으면 대신 스케줄링 해줌
   3. 다양한 플러그인 제공

### 설치

1. 베어 인스톨

   - 인스톨러를 사용해 PC나 서버에 설치

   - JRE 8, 11 만 지원

2. 컨테이너

   - `docker pull jenkins/jenkins:lts`
   - 컨테이너에 JRE가 포함
   - docker 컨테이너에 대한 이해 필요

3. Live 사연

   - docker-hub => jenkins/jenkins

   

### Docker file

Dockerfile

1 2 3 4 5 6 7 8

```
FROM jenkins/jenkins COPY ~~.pem /var/jenkins_home USER root RUN chmod 600 /var/jenkins_home/~~.pem RUN apt-get update RUN apt-get install -y python RUN apt-get install -y npm 
```

### shell

```
docker build -t jenkins. docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins:1.0
```

### Jenkins 관리 - Credentials

Jenkins store -> add credentials

username: email

pasword: pwd

id: ~~

### 새로운 Item (pipe line) - Script

- 파이프라인을 쓰면 중간 과정을 볼 수 있다.

```
pipeline{    agent any        stages{        stage("prepare"){            steps{                git credentialsId: "ssafy", url: "~~"                sh "npm install"            }        }                stage("build"){            steps{            sh "npm run build"                        }            post{                success{                    sh "scp -i /var/jenkins_home/~~.pem -q -o StrictHostKeyChecking=no -r ./dist/ ubuntu@~~~.io:/home.ubuntu/test"                    echo "Success"                }            }        }    } }
```

### 간단하게 확인

```
sudo python3 -m http-.server 8000
```

### 시나리오

- gitlab -> pull into container
- npm install => npm run build
- copy dist ./ ec2

