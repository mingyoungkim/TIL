<template>
  <div 
    class="alert toast-box" 
    :class="`alert-${msgType}`"
    role="alert"
  >
    {{ message }}
  </div>
</template>

<script>
export default {
  props: {
    message: {
      type: String,
      required: true,
    },
    msgType: {
      type: String,
      default: 'success',
    }
  }
}
</script>

<style>
  .toast-box {
    position: fixed;
    top: 10px;
    right: 10px;
  }
</style>