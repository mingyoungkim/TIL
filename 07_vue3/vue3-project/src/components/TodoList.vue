<template>
  <!-- 2. Router & 이벤트 버블링 -->
  <div
    v-for="(todo, idx) in todoList"
    :key="todo.id"
    class="card mt-2"
  >
    <!-- todo 클릭시, 해당 todo 페이지로 이동 -->
    <div 
      class="card-body p-2 d-flex align-items-center"
      style="cursor: pointer;"
      @click="moveToPage(todo.id)"
    >
      <!-- check box @change가 상위 클릭이벤트로인해 작동 안한 -->
      <!-- 현재, 클릭이벤트가 먼저 전파가 되고, 해당 이벤트가 끝난후, change이벤트가 전파되기때문 -->
      <!-- click event 방지 -->

      <!-- 개선 : 확실한 이벤트 타깃의 값을 보내주자! -->
      <div class="form-check flex-grow-1">
        <input 
          type="checkbox" 
          class="form-check-input" 
          :checked="todo.completed"
          @change="toggleTodo(idx, $event)"
          @click.stop
        >

        <label 
          class="form-check-label" 
          :style="todo.completed ? todoListtyle : {}" 
          :class="{ todo : !todo.completed }">
          {{ todo.subject }}
        </label>
      </div>
      <div>
        <!-- 이벤트버블링 방지 '이벤트.stop'-->
        <button 
          class="btn btn-danger btn-sm" 
          @click.stop="deleteTodo(idx)"
        >
          Delete
        </button>
      </div>
    </div>
  </div>
  
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  props: {
    todoList: {
      type: Array,
      required: true,
    }
  },
  emits: ['toggle-todo', 'delete-todo'],

  setup(props, { emit }) {
    const router = useRouter();
    const toggleTodo = (index, event) => {
      // event가 발생한 타겟의 체크 true, false 보내주기
      emit('toggle-todo', index, event.target.checked);

    };

    const deleteTodo = (index) => {
      emit('delete-todo', index);
    };

    const todoListtyle = {
      
    };

    const moveToPage = (todoId) => {
      // 1. router path 를 사용해서 원하는 페이지로 이동
      router.push('/todos/'+todoId);

      // 2. router name 을 사용해서 원하는 페이지로 이동
      /*
      router.push({
        name: 'Todo',
        params: {
          id: todoId
        }
      });
      */
    }

    return {
      toggleTodo,
      deleteTodo,
      moveToPage,
      todoListtyle,
    }
  }
}
</script>

