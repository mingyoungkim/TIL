<template>
  <!---------- 1. To do 추가 Form ---------->
  <!-- vue3 에서는 큰 빈 div 태그 생성 필요 없음 -->

  <!-- <div class="name"> -->
  <div v-bind:class="nameClass">

      <!-- 함수이기 때문에 `()` 필요 -->
    <!-- {{ greeting('welcome to') }} -->
    {{ greet }}
      <!-- template에서는 name.value로 접근 안해도 됨 -->
    {{ name }}
  </div>

  <!-- 단방향 바인딩 예시 -->
    <!-- input의 원래 있는 속성인 value에 name을 bind시켜주기 -->
    <!-- v-bind:속성 => 모든 속성 bind 가능 -->
  <!-- <input v-bind:type="type" v-bind:value="name"> -->

    <!-- v-bind 약어 => :속성 -->
  <!-- 양방향 바인딩 예시 1 : event 사용 -->
  <input 
    :type="type" 
    :value="name"
    @input="updateInputVal"
  >

  <!-- 양방향 바인딩 예시 2 : v-model 사용 -->
  <input type="text" v-model="name">

  <!-- <button class="btn btn-primary" v-on:click="updateName">Click</button> -->
  
    <!-- v-on 약어 => @click -->
  <button 
    class="btn btn-primary" 
    @click="onSubmit"
  >
    Click
  </button>



</template>


<script>
// vue 패키지에서 ref 를 import
import { ref } from 'vue';

export default {
  setup() {
    // const name = 'Mini World';
      // 1. const 는 변경 불가 => let으로 사용
    // let name = 'Mini World';
      // 2. let으로 바꿔서 updateName 해도 변수만 변경되지, 탬플릿에서 바뀐 변수가 show 되지는 않음 => ref로 변경
    const name = ref('Mini World');
    const type = ref('text');
    const nameClass = ref('name');
    const welcome = 'welcome to';

    // 함수 만들기
    const greeting = (welcom) => {
      return 'Hello, ' + welcom;
    }

    const greet = greeting(welcome);

    // 단방향 바인딩
    const updateName = () => {
      // name = 'MiniGom';
        // ref 사용하는 경우, 선언된 변수명.value
      name.value = 'MiniGom';
    };

    // 양방향 바인딩
    const onSubmit = () => {
    };

    // onInput 이벤트에서 event를 받아올 수 있음 (이벤트에 대한 정보들 담고 있음)
    const updateInputVal = (e) => {
      console.log(e.target.value);
      name.value = e.target.value;
    };

    // object return (template에서 접근할 수 있도록)
    return {
      name,
      greeting,
      greet,
      updateName,
      type,
      nameClass,
      onSubmit,
      updateInputVal
    };
  }  
}
</script>

<style>
  .name {
    color: plum;
  }
</style>
