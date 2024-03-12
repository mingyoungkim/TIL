<template>
  <!---------- 5. Json Server + async/await ---------->

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
    <div style="color:red">{{ error }}</div>

    <div v-if="!todos.length">
      추가된 Todo가 없습니다.
    </div>
    <div v-if="todos.length && !filterTodos.length">
      검색된 Todo가 없습니다.
    </div>

    <TodoList :todoList="filterTodos" @toggle-todo="toggleTodo" @delete-todo="deleteTodo" />

  </div>

</template>


<script>
import { ref, computed } from 'vue';
import TodoSimpleForm from './components/TodoSimpleForm.vue';
import TodoList from './components/TodoList.vue';
import axios from 'axios';

export default {
  components: {
    TodoSimpleForm,
    TodoList,
  },
  setup() {
    const todos = ref([]);
    const searchText = ref('');
    const error = ref('');

    const filterTodos = computed(() => {
      if (searchText.value) {
        return todos.value.filter(todo => {
          return todo.subject.includes(searchText.value);
        });
      }
      return todos.value;
    });

    const getTodos = async() => {
      try {
        // 모든 todos 데이터 가져오기
        const res = await axios.get('http://localhost:3000/todos');
        console.log(res);
        // get 해온 res.data가 배열이므로 '=' (push 아님)
        todos.value = res.data;
      }
      catch(err) {
        console.log(err);
      }
    };

    getTodos();

    /*
    const addTodo = (todo) => {
      error.value = '';
      // 데이터베이스 todo를 저장
      axios.post('http://localhost:3000/todos', {
        // json server를 사용하면 id를 보내지 않아도 db에서 저절로 추가해줌 (mySql 등 이하동문)
        subject: todo.subject,
        completed: todo.completed
      }).then(res => { 
        console.log(res);
        todos.value.push(todo) // 응답 온 후 성공적인 경우 실행
      }).catch(err => {
        console.log(err); // 응답 온 후 실패한 경우 실행
        error.value = 'Something went worg:('
      }); 
    };
    */

    ////////// async/await 로 구현 //////////
    const addTodo = async(todo) => {
      error.value = '';
      // try/catch => .then()/.catch() 역할을 함
      try {
        // await : 해당 axios 결과를 기다린다.
        const res = await axios.post('http://localhost:3000/todos', {
          subject: todo.subject,
          completed: todo.completed
        }); 
        todos.value.push(res.data);
      }
      catch(err) {
        error.value = 'Something went worg:('
      }
    };

    const toggleTodo = async(idx) => {
      const id = todos.value[idx].id;
      try {
        await axios.patch('http://localhost:3000/todos/'+id, {
          completed: !todos.value[idx].completed
        });
        todos.value[idx].completed = !todos.value[idx].completed;
      }
      catch(err) {
        console.log(err);
      }
    };

    const deleteTodo = async(idx) => {
      const id = todos.value[idx].id;
      try {
        await axios.delete('http://localhost:3000/todos/'+id);
        todos.value.splice(idx, 1);
      }
      catch(err) {
        console.log(err);
      }
      
    };

    return {
      todos,
      searchText,
      deleteTodo,
      addTodo,
      toggleTodo,
      filterTodos,
      error,
      getTodos,
    };
  }  
}
</script>

<style>

</style>