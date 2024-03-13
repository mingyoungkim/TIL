# Vue3_vueRouter

## 

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