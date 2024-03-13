<template>
  <!---------- 7. Watch ---------->

  <div class="container">
    <h2>To-do List</h2>

    <!-- keyup.enter : enter 키를 치고 땠을때, 실행 -->
    <input
      class="form-control"
      type="text"
      v-model="searchText"
      placeholder="Search Todo"
      @keyup.enter="searchTodo"
    />
    <hr/>

    <TodoSimpleForm @add-todo="addTodo"/>
    <div style="color:red">{{ error }}</div>

    <div v-if="!todos.length">
      추가된 Todo가 없습니다.
    </div>
    <div v-if="todos.length && !todos.length">
      검색된 Todo가 없습니다.
    </div>

    <TodoList 
      :todoList="todos" 
      @toggle-todo="toggleTodo" 
      @delete-todo="deleteTodo" 
    />

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
import { ref, computed, watch } from 'vue';
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
    let timeout = null; // search 할때, 이전 요청 취소 시키기 위한 변수
    
    // current page 가 변경될때 실행하기
    // watch 는 현재 값, 그 전값을 인자로 받음
    watch(curPage, (curPage, prev) => {
      console.log(curPage, prev);
    });

    // enter 키는 대기안하고 바로 search 되도록
    const searchTodo = () => {
      clearTimeout(timeout);
      getTodos(1);
    };

    // 모든 페이지에 있는 todo를 watch로 search 하기
    watch(searchText, () => {
        // 검색을 할때마다 첫 페이지에서 보여주기
      // getTodos(1);
        // but, input에 타자를 칠때마다 tr 생성 => 한번에 tr 쏘기 : setTimeout
      clearTimeout(timeout); 
      timeout = setTimeout(() => {
        getTodos(1);
      }, 2000);
      
    });

    const pages = computed(() => {
      return Math.ceil(totalTodos.value/todoLimit);
    });

    const getTodos = async(page = curPage.value ) => {
      curPage.value = page;
      try {
        // 모든 페이지에 있는 todos에서 filter하기 + 내림차순 (sort)
        const res = await axios.get(`http://localhost:3000/todos?_sort=id&_order=desc&subject_like=${searchText.value}&_page=${page}&_limit=${todoLimit}`);
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
        await axios.post('http://localhost:3000/todos', {
          subject: todo.subject,
          completed: todo.completed
        }); 
        // 추가 후에도 한페이지에 최대 5개 보여주기위해 getTodos 재호출
        getTodos(1);
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
        // 삭제 후에도 한페이지에 최대 5개 보여주기위해 getTodos 재호출
        getTodos(1);
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
      error,
      getTodos,
      pages,
      curPage,
      totalTodos,
      searchTodo
    };
  }  
}
</script>

<style>

</style>