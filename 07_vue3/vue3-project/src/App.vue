<template>
  <!---------- 2. To do List 만들기 ---------->

  <div class="container">
    <h2>To-do List</h2>
    <!-- form 태그에 submit 걸면, submit 하면 화면 reload 됨 -->
    <!-- 이를 prevent 하면 됨 -->
    <form class="d-flex" @submit.prevent="onSubmit">
      <div class="flex-grow-1 mr-2">
        <input 
          class="form-control"
          type="text"
          v-model="todo"
          placeholder="Type new To-do"
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

    <!-- {{ todos }} -->

    <!--
    <div class="card my-2">
      <div class="card-body p-2">
        {{ todos[0].subject }}
      </div>
    </div>
    <div class="card">
      <div class="card-body p-2">
        {{ todos[1].subject }}
      </div>
    </div>
  -->

  <!-- v-for 로 카드 여러개 만들기 -->
  <!-- v-for 사용시, element 각각의 노드를 식별하기 위해 key binding 사용 (필수!) -->
  <div
    v-for="todo in todos"
    :key="todo.id"
    class="card mt-2"
  >
    <div class="card-body p-2">
      {{ todo.subject }}
    </div>
  </div>

  </div>

</template>


<script>
import { ref } from 'vue';

export default {
  setup() {
    const todo = ref('');
    const todos = ref([
      {id:1, subject: '휴대폰사기'},
      {id:2, subject: '장보기'}
    ]);

    const onSubmit = () => {
      // form의 submit 했을 때, reload하는 event prevent 해줌
      // vue 에서는 submit.prevent 하는 것을 권장
      // e.preventDefault();
      todos.value.push({
        id: Date.now(),
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
    color: plum;
  }
</style>
