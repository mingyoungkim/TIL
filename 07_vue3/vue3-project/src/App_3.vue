<template>
  <!---------- 3. Component ---------->
  <!-- 코드가 길어져 관리하기 어려워지므로 component를 사용 -->
  <!-- component를 사용하면 짧은 줄로도 해당 역할을 파악할 수 있음 -->
  
  <!-- 현재 App.vue 는 부모 컴포넌트 -->

  <div class="container">
    <h4>count : {{ count }}</h4>
    <h4>double Count Computed : {{ doubleCountComputed }}</h4>
    <h4>double Count Computed : {{ doubleCountComputed }}</h4>
    <h4>double Count Method : {{ doubleCountMethod() }}</h4>
    <h4>double Count Method : {{ doubleCountMethod() }}</h4>
    <button @click="count++">Add Cnt</button>

    <h2>To-do List</h2>

    <!-- 부모컴포넌트에서 사용되는 compenent : 자식 컴포넌트 -->
      <!-- 자식 컴포넌트에서 올려준 이벤트 받기 -->
    <TodoSimpleForm @add-todo="addTodo"/>

    <div v-if="!todos.length">
      추가된 Todo가 없습니다.
    </div>

    <!-- 자식 컴포넌트로 데이터 넘겨주기 -->
    <!-- 속성으로 원하는 이름을 기재하고 binding -->
      <!-- todoList : props로 보내는 이름 -->
      <!-- todos : props로 보낼 데이터 -->
    <TodoList :todoList="todos" @toggle-todo="toggleTodo" @delete-todo="deleteTodo" />

  </div>

</template>


<script>
import { ref, computed } from 'vue';
import TodoSimpleForm from './components/TodoSimpleForm.vue';
import TodoList from './components/TodoList.vue';

export default {
  // component 등록
  components: {
    TodoSimpleForm,
    TodoList,
  },
  setup() {
    const todos = ref([]);
    const count = ref(1);
    
    // computed : 다른 state를 의존할 때 사용하는 state (state처럼 값을 리턴)
      // count 와 같은 애들을 state라 한다....??????
      
    ////////// computed 와 함수의 차이점 //////////
    // 1. 인자
      // 1-1. 함수는 인자로 값을 받아와서 사용 가능 (computed는 인자로 값 받기 불가)
      // 1-2. computed는 computed 함수 안에 들어있는 reactive state 가 있을 때만, 해당 state가 변경될때만 실행이 되서 그 값을 변수에 저장
    // 2. 값
      // 2-1. computed는 값을 cache 함 (한번 값을 저장)
    const doubleCountComputed = computed(() => {
      console.log('computed');
      return count.value * 2;
    });

    const doubleCountMethod = () => {
      console.log('method');
      return count.value * 2;
    };
    ///////////////////////////////////////////
    
    // 자식 컴포넌트에서 받아온 데이터(todo -> object) 인자로 가져오기
    const addTodo = (todo) => {
      // console.log(todo);
      todos.value.push(todo);
    };

    const toggleTodo = (idx) => {
      // console.log("1....... " + todos.value[idx].completed);
      todos.value[idx].completed = !todos.value[idx].completed;
      // console.log("2....... " + todos.value[idx].completed);
    };

    const deleteTodo = (idx) => {
      todos.value.splice(idx, 1);
    };

    return {
      todos,
      count,
      deleteTodo,
      addTodo,
      toggleTodo,
      doubleCountComputed,
      doubleCountMethod,
    };
  }  
}
</script>

<style>

</style>