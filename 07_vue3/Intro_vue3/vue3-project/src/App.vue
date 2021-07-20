<template>
  <div>
    <div v-if="toggle">true</div>
    <div v-else>false</div>
    <button @click="onToggle">Toggle</button>
    <div class="container">
      <h2>Todo List</h2>
      <form @submit.prevent="onSubmit">
        <div class="d-flex">
          <div class="flex-grow-1 mr-2">
            <input
              class="form-control"
              type="text"
              placeholder="Type new to-do"
              v-model="todo"
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
      <div v-show="hasError" style="color:red">Error! This field cannot be empty</div>
      </form>
      <div
      class="card mt-2"
      v-for="todo in todos"
      :key="todo.id"
      >
        <div class="card-body p-2">
          <div class="form-check">
            <input
             class="form-check-input"
             type="checkbox"
             v-model="todo.completed"
            >
            <!-- Class 바인딩 중 Object Syntax -->
            <!-- object안에 key값으로 넣고 싶은 class name
              value에 Boolean 들어감
              value가 T면 key값인 class가 추가/ F면 추가 안됨 -->
            <label
             class="form-check-label"
             :class="{ todo: todo.completed }"
            >
             {{ todo.subject }}
            </label>
          </div>          
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
    const todos = ref([]);
    const hasError = ref(false);
    // style은 변경 될 일 없으니까 ref로 안해도 됨
    const todoStyle = {
      // css에서는 text-decoration 지금은 js
      textDecoration: 'line-through',
      color: 'gray'
    };

    const onSubmit = () => {
      if (todo.value === '') {
        hasError.value = true;
      } else {
        todos.value.push({
          id: Date.now(),
          subject: todo.value,
          completed: false,
        });
        hasError.value = false;
        todo.value = '';
      }      
    };

    const onToggle = () => {
      toggle.value = !toggle.value;    
    };    

    return {
      todo,
      todos,
      toggle,
      hasError,
      todoStyle,
      onSubmit,
      onToggle,
    };
    
  },
}
</script>

<style>
  .todo {
    color: gray;
    text-decoration: line-through;
  }
</style>