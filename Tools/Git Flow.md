# Git Flow

## 개발 협업툴

### Why Git?

- 협업 WorkFlow
- 서비스/제품 이력관리
- 커밋규칙과 정확한 메시지
- 코드 리뷰



### Git 저장소 구조

- Local
  - working directory
  - staging area
  - localrepo
- Remote
  - remote repo
- Command 명령어
  - `GIT CHEAT SHEET` 구글링



### Git Branch

- 줄기에서 뻗어져 나온 가지
- 코드 관리를 위해서 분기된 흐름을 만들어내는 용도
- 특정 커밋을 가르키고 있어서 pointer 같은 느낌
- 보통 branch에서 작업



### Git source tree

- git history가 담겨져있음
- commit tree를 잘 읽어서 git 프로젝트에서 문제 발생 시 빠르게 파악 가능
- 과거 시점으로 돌아가서 그 때의 상태 확인 가능



### Git Flow

- 기본 branch

  - Develop

    개발에 사용

  - Master

    출시에 사용

- 명령어

  `git branch` : branch 조회 (develop checkout 확인)

  `git flow featur start 브랜치이름` : branch 시작

  https://learngitbranching.js.org/?locale=ko

  https://onlywei.github.io/explain-git-with-d3/

  https://git-scm.com/book/ko/v2



### Git commit 사전 작업

- 전역(global) 설정

  `git config --global user.name "미니"`

  `git config --global user.email "mini.com"`

  `git config -1`

- 프로젝트별 설정

  깃헙 및 사용자 계정이 존재하니까 global로 설정이 힘든경우

  `git config user.name "미니"`

  `git config user.email "mini.com"`

- 정확한 커밋 만들기

  - commit massage



### .gitignore 관리

- 무거운 폴더

  node_modules

  key 값

  log, backup 파일