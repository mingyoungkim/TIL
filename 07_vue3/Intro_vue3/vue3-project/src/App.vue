<template>
  <div>Mini Coder</div>

  <div class="name">
    <!-- 함수는 괄호 불러서 호출해야함 -->
    {{ greeting(name)}}
  </div>

  <div>{{ greet }}</div>
  <button 
    class="btn btn-primary"
    v-on:click="updateName"
    >
    Click
  </button>
</template>

<script>
export default {
  setup() {
    // 필요한 로직 작성
    // const name = 'Mini Coder';
    // const는 재선언 불가 하므로 let으로 바꿔주자.
    let name = 'Mini Coder';

    // greeting이라는 변수에 함수를 넣는 로직
    // greeting 함수에 callname이라는 매개변수를 넣어서 함수안에서 그 매개변수를 사용 가능
    const greeting = (callname) => {
      return 'Hello '+ callname;
    };

    // name과 greeting 함수를 한번에 greet에 넣어서 return해서 나타낼 수도 있다.
    const greet = greeting(name);

    const updateName = () => {
      name = 'Cute Mini',
      console.log(name)
    }

    // return 해주면 template에서 사용 가능
    return {
      name,
      greeting,
      greet,
      updateName,
    };
  }  
}
</script>

<style>
  .name {
    color: violet
  }
</style>
