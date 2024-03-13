<template>
  <div class="container">
    <h2>To-do List</h2>

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
// vue는 웬만해서 상대경로보다는 절대경로로 명시해주기 (@ : 소스폴더 자체)
import TodoSimpleForm from '@/components/TodoSimpleForm.vue';
import TodoList from '@/components/TodoList.vue';
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
    
    watch(curPage, (curPage, prev) => {
      console.log(curPage, prev);
    });

    const searchTodo = () => {
      clearTimeout(timeout);
      getTodos(1);
    };

    watch(searchText, () => {
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