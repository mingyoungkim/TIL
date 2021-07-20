# Vue3_Todo Add

## Todo Add 하자

### 01. Event Prevent

[Vue.js 이벤트 수식어]: https://kr.vuejs.org/v2/guide/events.html#%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EC%88%98%EC%8B%9D%EC%96%B4

- `v-on` 이벤트에 **이벤트 수식어**를 제공

  - `.prevent`

    이벤트 전파가 중단

  - `.stop`

    이벤트가 페이지를 재로드 안함

  - `.capture`

    이벤트 리스너를 추가할 때 캡처모드를 사용

  - 등등

```vue
<template>
  <div class="container">
    <h2>To-Do List</h2>
    <!-- onsubmit Event -->
    <!-- button의 type을 submit으로 해주면 @click="onsubmit"과 같음 -->
    <!-- click 뿐만 아니라 enter도 인식 -->
    <!-- 이때, 추가될 때 form이 submit이 되면 reloading됨 (form의 특성) -->
    <!-- 그래서 새로고침을 방지하자 => event.preventDefault() -->
    <!-- vue.js에서는 @submit.prevent="onSubmit" 하면 됨 -->
    <form 
      class="d-flex"
      @submit.prevent="onSubmit"
    >
      <div class="flex-grow-1 mr-2">
        <input
          class="form-control"
          type="text"
          v-model="todo"
          placeholder="Type new to-do"
        >
      </div>

      <div>
        <button 
          class="btn btn-primary"
          type="submit"
        >
          Add
        </button>
      </div>
    </form>
    {{ todos }}
  </div>
  
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    // 처음에 시작할 때 empty string으로 값 주기
    const todo = ref('');
    // 추가된 todo 담아주기
    const todos = ref([]);

    const onSubmit = () => {
      // event의 기본적인 refresh하는 속성 예방
      // e.preventDefault();
      // todos에 객체를 추가시키기
      todos.value.push({
        // id는 unique해야 하니까 일단 time을 넣자
        id: Date.now(),
        // todo의 제목
        subject: todo.value
      });
    };
    
    return {
      todo,
      todos,
      onSubmit,
    };
  }  
}
</script>

<style>
  .name {
    color: violet
  }
</style>
```

