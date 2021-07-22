<template>
  <div>
    <div v-if="toggle">true</div>
    <div v-else>false</div>
    <button @click="onToggle">Toggle</button>
    <div class="container">
      <h2>Todo List</h2>
      <TodoSimpleForm/>
      <!-- Form 부분을 자식 컴포넌트에 넣어주기~ -->
      <!-- <form @submit.prevent="onSubmit">
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
      <div v-show="hasError" style="color:red">
        Error! This field cannot be empty
      </div>
      </form> -->
      <div v-if="!todos.length">
        추가된 Todo가 없습니다.
      </div>
      <div
      class="card mt-2"
      v-for="(todo, index) in todos"
      :key="todo.id"
      >
        <div class="card-body p-2 d-flex align-items-center">
          <div class="form-check flex-grow-1">
            <input
             class="form-check-input"
             type="checkbox"
             v-model="todo.completed"
            >
            <label
             class="form-check-label"
             :class="{ todo: todo.completed }"
            >
             {{ todo.subject }}
            </label>
          </div>
          <div>
            <button
             class="btn btn-danger btn-sm"
             @click="deleteTodo(index)"
            >
              Delete
            </button>
          </div>          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import TodoSimpleForm from './components/TodoSimpleForm.vue'

export default {
  components: {
    TodoSimpleForm
  },
  setup() {
    const toggle = ref(false);
    
    const todos = ref([]);
    

    const todoStyle = {
      textDecoration: 'line-through',
      color: 'gray'
    };

    const onSubmit = () => {
    //   if (todo.value === '') {
    //     hasError.value = true;
    //   } else {
    //     todos.value.push({
    //       id: Date.now(),
    //       subject: todo.value,
    //       completed: false,
    //     });
    //     hasError.value = false;
    //     todo.value = '';
    //   }      
    };

    const onToggle = () => {
      toggle.value = !toggle.value;    
    };    

    const deleteTodo = (index) => {
      todos.value.splice(index, 1)
    };

    return {
      todos,
      toggle,
      todoStyle,
      onSubmit,
      onToggle,
      deleteTodo
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