<template>
  <!-- 1. Router & Toast -->
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

  <Toast 
    v-if="showToast" 
    :message="toastMsg"
    :msgType="toastAlertType"
  />

</template>

<script>
import { ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import _ from 'lodash';
import Toast from '@/components/Toast.vue';

export default {
  components: {
    Toast,
  },
  setup() {
    const route = useRoute();
    const router = useRouter();
    // console.log(route.params);
    const todoId = route.params.id;
    const originTodo = ref(''); // todo 원래 값
    const todo = ref('');
    const loading = ref(true);
    const showToast = ref(false); // todo update 후, 성공적으로 업데이트 되었다는 toast alert 표시를 위한 변수
    const toastMsg = ref('');
    const toastAlertType = ref('');
    
    const getTodo = async() => {
      try {
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
      }
      catch(err) {
        triggerToast('Something went Wrong (' + err.message + ')', 'danger');
      }
      
    };

    const toggleTodoStatus = () => {
      todo.value.completed = !todo.value.completed;
    };

    const moveToList = () => {
      router.push('/todos');
    };

    const onSave = async() => {
      try {
        const res = await axios.put(`http://localhost:3000/todos/${todoId}`, {
          subject: todo.value.subject,
          completed: todo.value.completed
        });
        originTodo.value = { ...res.data };
        triggerToast('Successfully Saved');
      }
      catch(err) {
        triggerToast('Something went Wrong (' + err.message + ')', 'danger');
      }
      
    };

    const isTodoUpdated = computed(() => {
      return _.isEqual(todo.value, originTodo.value); // true OR false
    });

    // type 아무것도 안받으면 기본갑 : succuss
    const triggerToast = (msg, type='succsess') => {
      showToast.value = true;
      toastMsg.value = msg;
      toastAlertType.value = type;
      setTimeout(() => {
        showToast.value = false;
        toastAlertType.value = '';
        toastMsg.value = '';
      }, 3000);
    };

    getTodo();

    return {
      todo,
      loading,
      toggleTodoStatus,
      moveToList,
      onSave,
      isTodoUpdated,
      showToast,
      toastMsg,
      toastAlertType,
    }
  }
}
</script>

<style>

</style>