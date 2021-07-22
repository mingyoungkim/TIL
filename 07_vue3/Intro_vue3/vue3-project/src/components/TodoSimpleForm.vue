<template>
  <form @submit.prevent="onSubmit">
    <div class="d-flex">
      <div class="flex-grow-1 mr-2">
        <input
          class="form-control"
          type="text"
          placeholder="Type new to-do"
          v-model="todo"
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
    <div v-show="hasError" style="color:red">
      Error! This field cannot be empty
    </div>
  </form>
  
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const todo = ref('');
    const hasError = ref(false);

    const onSubmit = () => {
      if (todo.value === '') {
        hasError.value = true;
      } else {
        // todos.value.push({
        //   id: Date.now(),
        //   subject: todo.value,
        //   completed: false,
        // });
        hasError.value = false;
        todo.value = '';
      }      
    };

    return {
      todo,
      hasError,
      onSubmit,
    };
    
  },
}
</script>

<style>

</style>