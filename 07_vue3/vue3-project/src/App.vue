<template>
  <!---------- 4. 검색 기능 ---------->

  <div class="container">
    <h2>To-do List</h2>

    <input
      class="form-control"
      type="text"
      v-model="searchText"
      placeholder="Search Todo"
    />
    <hr/>

    <TodoSimpleForm @add-todo="addTodo"/>

    <div v-if="!todos.length">
      추가된 Todo가 없습니다.
    </div>
    <div v-if="todos.length && !filterTodos.length">
      검색된 Todo가 없습니다.
    </div>

    <!-- 검색된 애들만 내려줄 거니까 todos -> filterTodos -->
    <TodoList :todoList="filterTodos" @toggle-todo="toggleTodo" @delete-todo="deleteTodo" />

  </div>

</template>


<script>
import { ref, computed } from 'vue';
import TodoSimpleForm from './components/TodoSimpleForm.vue';
import TodoList from './components/TodoList.vue';

export default {
  components: {
    TodoSimpleForm,
    TodoList,
  },
  setup() {
    const todos = ref([]);
    const searchText = ref('');

    const filterTodos = computed(() => {
      if (searchText.value) {
        // filter() : js에서 기본으로 포함된 함수 (array에서 사용가능)
        return todos.value.filter(todo => {
          // includes() : js String 함수
          return todo.subject.includes(searchText.value);
        });
      }
      return todos.value;
    });

    const addTodo = (todo) => {
      todos.value.push(todo);
    };

    const toggleTodo = (idx) => {
      todos.value[idx].completed = !todos.value[idx].completed;
    };

    const deleteTodo = (idx) => {
      todos.value.splice(idx, 1);
    };

    return {
      todos,
      searchText,
      deleteTodo,
      addTodo,
      toggleTodo,
      filterTodos,
    };
  }  
}
</script>

<style>

</style>