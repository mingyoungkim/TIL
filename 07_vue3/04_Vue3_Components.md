# Vue3_Components

## 자식 컴포넌트 생성

### 01. 자식 컴포넌트 Import해서 출력시키기

- 하위 컴포넌트 생성

  ```vue
  <template>
    <h2>Todo Simple Form</h2>
  </template>
  
  <script>
  // component는 하나의 부품이라서 다른 곳에서 가져다 쓸 수 있음
  // TodoSimpleForm을 App.vue에서 불러서 사용하는 것을 구현해보자.
  export default {
    setup() {
      
    },
  }
  </script>
  
  <style>
  
  </style>
  ```



- 부모 컴포넌트에 작업

  1. Import 해오기
  2. Import한 component 등록

  ```vue
  <script>
  import { ref } from 'vue';
  // 1. TodoSimpleForm 가져다쓰기 위해 import
  import TodoSimpleForm from './components/TodoSimpleForm.vue'
  
  export default {
    // 2. import한 component를 등록하기
    // 등록하면 이제 이 component를 App.vue에서 사용가능해짐
    components: {
      TodoSimpleForm
    
    },
    setup() {
      
    },
  }
  </script>
  ```

  3. template에 보여주기

  ```vue
  <template>
    <!-- 3. tag처럼 template에 적어주면 화면에 출력됨 -->
    <TodoSimpleForm/>      
  </template>
  ```



### 02. Emit & Props

> Emit

