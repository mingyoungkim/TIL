<template>
  <div>
    <div class="container">

      <h2>Todo List</h2>
      <input
        class="form-control"
        type="text"
        placeholder="Search"
        v-model="searchText"
      >
      <hr/>

      <TodoSimpleForm @add-todo="addTodo"/>
      
      <div v-if="!todos.length">
        추가된 Todo가 없습니다.
      </div>

      <TodoList
       :todoList="todos" 
       @toggle-todo="toggleTodo" 
       @delete-todo="deleteTodo"
      />

    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import TodoSimpleForm from './components/TodoSimpleForm.vue'
import TodoList from './components/TodoList.vue'

export default {
  components: {
    TodoSimpleForm,
    TodoList
  },
  setup() {    
    const todos = ref([]);

    const addTodo = (todo) => {
      todos.value.push(todo)
    };

    const deleteTodo = (index) => {
      todos.value.splice(index, 1)
    };

    const toggleTodo = (index) => {
      todos.value[index].completed = !todos.value[index].completed;
    };

    const searchText = ref('');
    // filter가 된 todos의 값을 확인
    const filteredTodos = computed(() => {
      // searchText가 empty string이 아니면 filter가 된 array return
      if (searchText.value) {
        // filter는 js의 내장함수 (array에 쓸 수 있는 함수)
        return todos.value.filter();
      }
      // empty면 모든 todos 값 그대로 return
      return todos.value;
    });

    return {
      todos,
      searchText,
      deleteTodo,
      addTodo,
      toggleTodo,
      
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