# Jira

## 협업툴

### 용어정리

> JQL

- Jira Query Language
- Jira Issue를 구조적으로 검색 하기 위해 제공하는 언어
- SQL 문법과 비슷



> Issues

- Story : user 가 어떤 일을 해야하는지 스토리 가이드

  (사용자가 로그인을 한다)

- Task : 할일

  (로그인을 하기 위해서 그 로직을 구성해야함)

- Bug : 개발 후 버그 발생 시

- Epic : 하나의 큰 틀 

  - 이 안에 Task, Story, Bug 다 들어갈 수 있다.



> Issue 화면

- 제목 확인 필수
- Description : 자세한 설명
- Assignee : 담당자
- Reporter : 생성자
- Status
  - View Workfolw 확인하면 이 issue가 어떤 단계로 흘러가는지 설명
- Component
  - 하나의 개발 항목
  - Epic으로 묶기도 애매하고 마땅한 그룹 없을 때 Component로 묶어주면 됨
- Resolution
  - 이 Issue가 완료되었는지 여부



> 검색 기능

- Basic Query
  - 선택을 해서 간단하게 검색할 수 있는 기능

- Advanced Query
  - JQL 을 사용해서 상세 검색 가능
  - =, !=, >, >=
  - in, not in
  - ~ (contaions)
  - !~ (not contains)
  - is empty, is not empty, is null, is not null
  - 대표적인 JQL 함수
    - endOfDay(), endOfWeek() => `자정, 토요일`
    - startOfDay(), startOfWeek() => `정오, 일요일`



> 날짜 관련 기능

- Relative Dates
  - 현재는 Current
  - 오늘을 기준으로 -1d(어제), 1d(내일)



> Fiter Share

- 내가 검색한 이슈들을 남들도 똑같이 검색할 수 있도록 설정해놓는 것



### Dashboard

> System Dashboard

- 시스템 관리자가 사용자들이 처음 접속시 설정가능하도록
- 나만의 Dashboard 생성 가능
- Scrum 형태로 자동으로 생성
  - Sprint 주기
  - Backlog에 이슈들 다 담아놓고 이번 Sprint에는 어떤 이슈 해결할 지 그루핑
- gadget
  - 지표 관리를 위한 차트
  - 대표적
    - Assigned to Me == Filter Dashboard
    - pie Chart : 시각적으로 항목별로 확인 가능
    - Heat Map : 가장 많이 차지하고 있는 컴포넌트 확인



### Agile Board

> Kanban Board

- Issue OR Filter 토대로 생성 가능
- Sprint 라는 개념 없이 현재 조회된 이슈들을 단계대로 어떻게 진행되고 있는지 확인
- 상태도 확인 (Todo, Done 몇개씩인지 확인 가능)
