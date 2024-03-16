<template>
  <h1>Todo Page</h1>
  <div v-if="loading">Loding...</div>
  
  <form @submit.prevent="onSave">
    <div class="row">
      <div class="col-6">
        <div class="form-group">
          <label>Subject</label>
          <input 
            v-model="todo.subject" 
            type="text" 
            class="form-control"
          >
        </div>
      </div>
      <div class="col-6">
        <div class="form-group">
          <label>Status</label>
          <div>
            <button 
              type="button"
              class="btn"
              :class="todo.completed ? 'btn-success' : 'btn-danger'"
              @click="toggleTodoStatus"
            >
              {{ todo.completed ? 'Completed' : 'InCompleted' }}
            </button>
          </div>
        </div>
      </div>
    </div>
    
    <!-- todo 가 변경된 경우만 활성화 -->
    <button 
      type="submit" 
      class="btn btn-primary"
      :disabled="isTodoUpdated"
    >
      SAVE
    </button> 
    <button 
      type="submit" 
      class="btn btn-outline-dark ml-2"
      @click="moveToList"
    >
      CANCEL
    </button> 
  </form>
</template>

<script>
import { ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import _ from 'lodash';

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();
    // console.log(route.params);
    const todoId = route.params.id;
    const originTodo = ref(''); // todo 원래 값
    const todo = ref('');
    const loading = ref(true);
    
    const getTodo = async() => {
      const res = await axios.get('http://localhost:3000/todos/'+todoId);
      /* 
        originTodo, todo 둘 다 같은 주소값을 가지게 되면 하나가 바뀌면 둘 다 변경됨
        => spread operator를 사용
      */
      // originTodo.value = res.data;
      // todo.value = res.data;
      originTodo.value = { ...res.data };
      todo.value = { ...res.data };
      loading.value = false;
      // console.log(todo.value.completed);
    };

    const toggleTodoStatus = () => {
      todo.value.completed = !todo.value.completed;
    };

    const moveToList = () => {
      router.push('/todos');
    };

    const onSave = async() => {
      const res = await axios.put(`http://localhost:3000/todos/${todoId}`, {
        subject: todo.value.subject,
        completed: todo.value.completed
      });
      originTodo = { ...res.data };
    };

    const isTodoUpdated = computed(() => {
      return _.isEqual(todo.value, originTodo.value); // true OR false
    });

    getTodo();

    return {
      todo,
      loading,
      toggleTodoStatus,
      moveToList,
      onSave,
      isTodoUpdated,
    }
  }
}
</script>

<style>

</style>