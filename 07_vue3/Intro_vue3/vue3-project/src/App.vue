<template>
  <!-- oninput Event => user가 input field에 뭔가를 쓸 때 실행 -->
  <input
   type="text"
   v-model="name"
  >

  <button 
    class="btn btn-primary"
    @click="onSubmit"
    >
    Click
  </button>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const name = ref('Mini Coder');

    const onSubmit = () => {
      console.log(name.value)
    };
    
    return {
      name,
      onSubmit,
    };
  }  
}
</script>

<style>
  .name {
    color: violet
  }
</style>