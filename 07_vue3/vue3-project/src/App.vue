<template>
  <!---------- 2. To do List 만들기 ---------->

  <!-- v-show : 처음에는 두개다 rendering -->
  <!-- 값에 따라 style에 display 처리됨 -->
  <div v-show="toggle">true</div>
  <div v-show="!toggle">false</div>

  <!-- v-if : 애초에 rendering 할때, 조건에 맞는 애만 display -->
  <div v-if="toggle">true</div>
  <div v-else>false</div>
 
  <!-- v-if 는 토글하는데 , v-show는 렌더링하는데 소비됨
    v-show는 토글을 자주할때 사용
    v-if 는 조건이 잘 바뀌지 않을 때 사용 -->
  <button @click="onToggle">Toggle</button>

  <div class="container">
    <h2>To-do List</h2>
    <!-- form 태그에 submit 걸면, submit 하면 화면 reload 됨 -->
    <!-- 이를 prevent 하면 됨 -->
    <form @submit.prevent="onSubmit">
      <div class="d-flex">
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
      </div>
      <!-- 자주 사용될 애라서 v-show 로 사용 -->
      <div v-show="hasError" style="color: red;">
        This field cannot be empty
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
  <div v-if="!todos.length">
    추가된 Todo가 없습니다.
  </div>
  <div
    v-for="(todo, idx) in todos"
    :key="todo.id"
    class="card mt-2"
  >
    <div class="card-body p-2 d-flex align-items-center">
      <div class="form-check flex-grow-1">
        <input type="checkbox" class="form-check-input" v-model="todo.completed">
        <!-- stlye bind -->
        <!-- class bind -->
        <label 
          class="form-check-label" 
          :style="todo.completed ? todoStyle : {}" 
          :class="{ todo : !todo.completed }">
          {{ todo.subject }}
        </label>
      </div>
      <div>
        <button class="btn btn-danger btn-sm" @click="deleteTodo(idx)">
          Delete
        </button>
      </div>
    </div>
  </div>

  </div>

</template>


<script>
import { ref } from 'vue';

export default {
  setup() {
    const toggle = ref(false);
    const todo = ref('');
    const todos = ref([
      // {id:1, subject: '휴대폰사기'},
      // {id:2, subject: '장보기'}
    ]);
    const hasError = ref(false);
    // style은 변경 될일 없어서 ref로 안해도 됨
    const todoStyle = {
      // css 에서는 text-decoration인 style을 js에서는 camelCase로
      textDecoration: 'line-through',
      color: 'gray'
    }

    const onSubmit = () => {
      if (todo.value === '') {
        hasError.value = true;
      }
      else {
        // form의 submit 했을 때, reload하는 event prevent 해줌
        // vue 에서는 submit.prevent 하는 것을 권장
        // e.preventDefault();
        todos.value.push({
          id: Date.now(), // todo 의 key
          subject: todo.value, // todo 이름
          completed: false, // todo의 완료여부
        });
        hasError.value = false;
        todo.value = '';
      }
    };

    const onToggle = () => {
      toggle.value = !toggle.value;
    }

    const deleteTodo = (idx) => {
      // idx로 부터 1개만 지워주기
      todos.value.splice(idx, 1);
    }

    return {
      toggle,
      todo,
      todos,
      hasError,
      todoStyle,
      onSubmit,
      onToggle,
      deleteTodo
    };
  }  
}
</script>

<style>
  .todo {
    color: plum;
    font: bold;
  }
</style>
