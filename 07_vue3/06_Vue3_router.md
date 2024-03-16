# Vue3_vueRouter

## Router

### 01. 설치단계

[설치환경] : https://v3.router.vuejs.org/kr/installation.html

  - `npm install vue-router` 

* router 기본 js

```js
import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
  history: '',
  routes: [
    {
      path: '', // url
      name: '', // 이름
      component: '' // 해당 컴포넌트
    },
    {}
  ]
});

export default router;
```

* main.js

```js
  import router from './router';

  createApp(App).use(router).mount('#app')
```

### 02. router를 이용한 페이지 이동
> 리로딩 없는 페이지 이동 (새로고침 X) 

```vue
  <template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <!-- a태그의 href : 페이지 이동 => vue 에서 페이지 이동은 지양 (다운받았던 것을 다시 다운받게됨) -->
      <!-- a태그보다 페이지이동은 빠르지만, 앱이 커질수록 처음 구동하는데 속도가 느려질 수는 있음 (맨처음에 모든 파일들을 데려오기 때문) -->
      <!-- <a class="navbar-brand" href="/">Mini Home</a> -->

      <!-- 1. router index.js에 설정한 path로 이동 -->
      <router-link class="navbar-brand" to="/"> 
      <!-- <router-link class="navbar-brand" :to="{ name: 'Home' }"> --> 
        Mini Home
      </router-link>

      <!--
            2. router index.js에 설정한 name 으로 이동 
      <router-link class="navbar-brand" :to="{ name: 'Home' }"> 
        Mini Home
      </router-link>
      -->      

      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <!-- <a class="nav-link" href="/todos">Todos</a> -->
          <router-link class="nav-link" to="/todos">
            Todos
          </router-link>
        </li>
      </ul>
    </nav>
    <!-- router-view 넣어주면, 페이지를 이동할때마다 router-view에 homeComponet 가 들어가게됨 -->
    <router-view/>
  </template>
```

### 03. router 작동원리

1. 작성한 코드 compile 후 서버에 배포 (html, js 파일들이 저장이 됨)

2. 해당 도메인에 접속하면, 연결한 서버에 요청

3. html(public > index.html), js(js file, vue) 파일들을 다운을 받아 뿌려줌

4. 페이지 이동시, 내부적으로는 a태그를 사용하고 있지만 새로고침하면서 요청보내는 것을 router에서 중간에 가로챔
  (url을 router의 link와 비교해서 일치하는 컴포넌트를 넣어줌)

### 04. use router

* useRoute : 현재 활성 라우트 정보에 접근할 수 있다. (읽기 전용)

* useRouter : 라우터 인스턴스로 javascript에서 다른 페이지로 이동할 수 있다.

### 05. 이벤트 버블링
> 클릭이벤트가 거품처럼 부모의 부모의 부모에 있는 클릭이벤트까지 실행되는 현상

* 자식 태그에 클릭이벤트가 발생되면 최상위 부모 태그까지 올라가서 모든 클릭이벤트 실행시킴 (js 클릭이벤트의 특성)

* 방지 

  - stop propagation

  ```vue
  <!-- 이벤트버블링 방지 '이벤트.stop'-->
    <button 
      class="btn btn-danger btn-sm" 
      @click.stop="deleteTodo(idx)"
    >
      Delete
    </button>
  </div>
  ```

✍ js 자료형

1. 원시타입
> 숫자, 문자, boolean, undefined

  ```js
  // 원시타입은 값 자체를 변수에 담음
    a = 4;
    b = 4;
    a === b; // true

  ```

2. 참조타입
> Object, Array, Function

  ```js
  // 참조타입은 메모리에 주소의 값을 변수에 담음
    c = {a : 1};
    d = {a : 1};
    // 두 객체의 주소 값을 비교하므로 false
    c === d; // false
    e = d;
    // e는 객체의 메모리 주소의 값까지 복사해서 담았기 때문에 true
    d === e; // true
    c === e; // false
    d.a = 2; // e.a 도 함께 변경됨 (같은 주소를 바라보고 있기 때문)

    // d의 주소값은 제외하고 값만 복사하고 싶다면,, spread operator 사용
    f = {...d};
    d === f; // false
    d.a === f.a; // true
    JSON.stringify(d) === JSON.stringify(f); // true
  ```

* `lodash`
> js library

  - `npm install lodash`

```js
  a = {id: '1', name: 'mini'};
  b = {name: 'mini', id: '1'};
  // json 안의 내용 순서들이 다른경우, JSON.stringify 로 비교하면 false
  JSON.stringify(a) === JSON.stringify(b); // false

  // 제대로 값을 비교하기 위해 lodash 라이브러리 사용하기
  var el = document.createElement('script');
  el.src = "https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.21/lodash.min.js";
  el.type = "text/javascript";
  document.head.appendChild(el);
  _.isEqual(a, b); // true
```