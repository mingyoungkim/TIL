<template>
  <!-- 2. Life Cycle & 메모리 누수 관리 -->
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
import { ref, computed, onUnmounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import _ from 'lodash';
import Toast from '@/components/Toast.vue';
import { useToast } from '@/composables/toast';

export default {
  components: {
    Toast,
  },
  setup() {
    const route = useRoute();
    const router = useRouter();
    const todoId = route.params.id;
    const originTodo = ref(''); 
    const todo = ref('');
    const loading = ref(true);
    
    /********** 반복되는 Toast 에 대한 로직 => composables 사용하여 해당 로직 따로 빼기 **********/
    // const showToast = ref(false); 
    // const toastMsg = ref('');
    // const toastAlertType = ref('');
    // const timeout = ref('');
    // const triggerToast = (msg, type='succsess') => {
    //   showToast.value = true;
    //   toastMsg.value = msg;
    //   toastAlertType.value = type;
    //   /* setTimeout
    //     setTimeout 은 메모리에 올라감
    //     so, 해당 컴포넌트가 페이지이동을 하여 unMounted 되어도 setTimeout 이 메모리에 올라가 있음
    //     => 관리 해줘야함
    //     => setTimeout 결과 값을 timeout 변수에 넣기
    //   */
    //   timeout.value = setTimeout(() => {
    //     showToast.value = false;
    //     toastAlertType.value = '';
    //     toastMsg.value = '';
    //   }, 3000);
    // };
    const {
      showToast,
      toastMsg,
      toastAlertType,
      triggerToast,
    } = useToast();

    onUnmounted(() => {
      // 해당 컴포넌트가 unmount 되면서 timeout value 초기화
      clearTimeout(timeout.value);
    });
    
    const getTodo = async() => {
      try {
        const res = await axios.get('http://localhost:3000/todos/'+todoId);
        originTodo.value = { ...res.data };
        todo.value = { ...res.data };
        loading.value = false;
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
      return _.isEqual(todo.value, originTodo.value); 
    });

    

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