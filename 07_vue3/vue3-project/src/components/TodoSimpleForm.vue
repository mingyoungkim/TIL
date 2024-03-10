<template>
  Todo Simple Form
  <form @submit.prevent="onSubmit">
    <div class="d-flex">
      <div class="flex-grow-1 mr-2">
        <input 
          class="form-control"
          type="text"
          v-model="todo"
          placeholder="Type new To-do"
        >
      </div>
      <div>
        <button 
          class="btn btn-primary" 
          type="submit"
        >
        Add
        </button>
      </div>  
    </div>
    <div v-show="hasError" style="color: red;">
      This field cannot be empty
    </div>
  </form>
</template>

<script>
import { ref } from 'vue';

export default {
  // Composition API 사용시, 두개의 object 인자를 받아옴 
    // 1. context : 자식 컴포넌트에서 부모 컴포넌트로 데이터 보낼때 필요한 emit 함수를 context에서 사용
    // 2. props : 부모 컴포넌트에서 자식 컴포넌트로 데이터 보낼때 사용
  emits: ['add-todo'],
  setup(props, context) {
    const todo = ref('');
    const hasError = ref(false);

    const onSubmit = () => {
      if (todo.value === '') {
        hasError.value = true;
      }
      else {
        // 부모 컴포넌트의 todos Array에 추가해줘야함 (부모 컴포넌트로 이벤트를 보내주기)
          // 1. 이벤트 이름 2. 보낼 데이터 (지금은 object 보내줌)
        context.emit('add-todo', {
          id: Date.now(), 
          subject: todo.value, 
          completed: false, 
        });
        hasError.value = false;
        todo.value = '';
      }
    };

    return {
      todo,
      hasError,
      onSubmit,
    }
  },
}
</script>

<style>

</style>
