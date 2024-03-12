# Vue3_JsonServer_Async_Watch

## JsonServer로 데이터 저장 (개발시에만 사용 가능)

> 가짜 데이터베이스 패키지 (fake RestAPI)

### 01. 설치단계

[설치환경] : https://www.npmjs.com/package/json-server

  - `npm install -D json-server@0.17.4` (버전이슈)

  - db.json 파일 생성 (데이터베이스 테이블과 같은 형태)

  - start json server : `npx json-server --watch db.json`

### 02. axios 패키지 설치

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

* Pagination
  - 예시 : GET /posts?_page=1&_per_page=25

## Watch

  1. watchEffect

    > 데이터 변경 감지

    - vue 패키지에서 watchEffect import (vue3 에서 추가됨)

    - watchEffect 함수 안에 reactive state(ref, computed, props 등등) 가 있고, 그 값이 변경되면 해당 로직 재실행

    ```vue
    <script>
      import { watchEffect } from 'vue';

      export default {
        const test = ref('hi');

        setup() {
          watchEffect(() => {
            console.log(test);
          });
        }
      }
    </script>
    ```

  2. watch

    > watchEffect 와 비슷하게 reactive state를 지켜보다가 update가 되는 것을 감지하고 어떤 로직을 수행

    * watch 는 현재 값, 그 전값을 인자로 받음

    - 방법
      - 한 개의 소스 지켜봄

      ```vue
      <script>
        import { reactive, watch } from 'vue';

        export default {
          const test = reactive({
            a: 1
          })

          setup() {
            watch(() => test.a, (curData, prev) => {
              console.log(curData, prev);
            });
            test.a = 10;
          }
        }
      </script>
      ```

      - 여러개의 소스 지켜봄

      ```vue
      <script>
        import { ref, reactive, watch } from 'vue';

        export default {
          const test = reactive({
            a: 1,
            b: 2
          })
          const test2 = ref('');
          const test3 = ref('');

          setup() {
            // reactive 여러개 watch
            watch(() => [test.a, test.b], (curData, prev) => {
              console.log(curData, prev);
            });
            test.a = 10;

            // ref 여러개 watch
            watch([test1, test2], (curData, prev) => {
              console.log(curData, prev);
            });
          }
        }
      </script>
      ```