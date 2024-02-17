<template>
  <!-- vue3 에서는 큰 빈 div 태그 생성 필요 없음 -->
  <div class="name">
    <!-- 함쉬이기 때문에 () 필요 -->
    <!-- {{ greeting('welcome to') }} -->
    {{ greet }}
    {{ name }}
  </div>
  <div>HI</div>
</template>

<script>
export default {
  setup() {
    const name = 'Mini World';
    const welcome = 'welcome to';

    // 함수 만들기
    const greeting = (welcom) => {
      return 'Hello, ' + welcom;
    }

    const greet = greeting(welcome);

    // object return (template에서 접근할 수 있도록)
    return {
      name,
      //greeting,
      greet
    }
  }  
}
</script>

<style>
  .name {
    color: plum;
  }
</style>
