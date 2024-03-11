# Vue3_JsonServer

## JsonServer로 데이터 저장 (개발시에만 사용 가능)
> 가짜 데이터베이스 패키지 (fake RestAPI)

### 01. 설치단계
[설치환경] : https://www.npmjs.com/package/json-server

1. 설치

  - `npm install -D json-server@0.17.4` (버전이슈)

  - db.json 파일 생성 (데이터베이스 테이블과 같은 형태)

  - start json server : `npx json-server --watch db.json`

### 02. 패키지 설치

1. axios 설치

> http request 를 보낼때 사용하는 npm 패키지

  - `npm i axios`

* axios.post(request 보낼 url, 보낼 data)
* axios.get(request 보낼 url)
* axios.patch(request 보낼 url, 수정할 data)

* PUT : 데이터 전체 수정 / PATCH : 부분적 변경


* js 요청은 비동기적으로 일어남 
  - request 보내고 나면 promise 라는 것으로 응답옴
  - 해당 응답이 오기전에 다음으로 넘어감
  - so, 응답이 왔을 때 행위를 하도록 해야함 : .then() or async / await

* 동기 : 순차적으로 일어남, 비동기 : 순서가 바뀔 수 있음

### 03. 


