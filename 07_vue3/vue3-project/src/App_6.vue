<template>
  <!---------- 6. Pagination ---------->

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

    <TodoList 
      :todoList="filterTodos" 
      @toggle-todo="toggleTodo" 
      @delete-todo="deleteTodo" 
    />
    <!-- bootstrap pagination -->
    <nav aria-label="Page navigation example">
      <ul class="pagination">
        <li v-if="curPage !== 1" class="page-item">
          <a style="cursor: pointer;" class="page-link" href="#" @click="getTodos(curPage-1)">Previous</a>
        </li>

        <li 
          class="page-item" 
          v-for="page in pages" 
          :key="page" 
          :class="curPage === page ? 'active' : ''"
        >
          <!-- v-for로 돌리면서 값을 getTodos로 넘김 -->
          <a class="page-link" href="#" @click="getTodos(page)">{{ page }}</a>
        </li>
        
        <li class="page-item" v-if="curPage !== pages">
          <a style="cursor: pointer;" class="page-link" href="#" @click="getTodos(curPage+1)">Next</a>
        </li>
      </ul>
    </nav>

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
    const totalTodos = ref(0); // 총 데이터 갯수
    const todoLimit = 5; // 한 페이지 당 보여줄 데이터 갯수
    const curPage = ref(1); // 현재페이지

    const pages = computed(() => {
      // ceil : 올림
      return Math.ceil(totalTodos.value/todoLimit);
    });

    const filterTodos = computed(() => {
      if (searchText.value) {
        return todos.value.filter(todo => {
          return todo.subject.includes(searchText.value);
        });
      }
      return todos.value;
    });

    const getTodos = async(page = curPage.value ) => {
      curPage.value = page;
      try {
          // Page 첫 페이지, 최대 5개 보여주기
        // const res = await axios.get('http://localhost:3000/todos?_page=1&_limit=5');
          // 백틱으로 js 변수 사용해서 url 지정 (ref인 경우 .value로 접근) 
        // const res = await axios.get(`http://localhost:3000/todos?_page=${curPage.value}&_limit=${todoLimit}`);
          // page 인자로 받기
        const res = await axios.get(`http://localhost:3000/todos?_page=${page}&_limit=${todoLimit}`);
        // x-total-count : 총 데이터의 갯수
        // res.headers.x-total-count => '-' 데시가 들어간 경우, '.'으로 접근 불가
        console.log(res.headers['x-total-count']);
        totalTodos.value = res.headers['x-total-count'];
        todos.value = res.data;
      }
      catch(err) {
        console.log(err);
      }
    };

    getTodos();

    const addTodo = async(todo) => {
      error.value = '';
      try {
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
      pages,
      curPage,
      totalTodos,
    };
  }  
}
</script>

<style>

</style>