# Vue3_computed

## computed를 이용해서 searchBar 만들기

### 01. computed란?

> 정의

- 다른 state를 의존할 때 사용하는 state

- 어떤 값을 계속 감시함

- 그냥 함수와의 차이점

  1. `함수`=> 인자로 값을 받아와서 사용 가능

     `computed`=> 불가능

  2. `computed`는 computed함수 안에 들어있는 reactive state가 있을 때만, 

     그리고 reactive state가 변경될 때만 실행이 되서 그 값을 변수에 저장

  3. `computed`는 값을 캐시를 함

     그래서 한 번 계산하면 그 값을 저장

```vue
<template>
  <div>
    <div class="container">
      <h4>count: {{ count }}</h4>
      <!-- computed는 값이 return 되므로 state처럼 바로 사용 가능 -->
      <h4>double count computed: {{ doubleCountComputed }}</h4>
      <!-- doubleCountMethod는 함수니까 호출해야해서 괄호 필요 -->
      <h4>double count method: {{ doubleCountMethod() }}</h4>
      <button @click="count ++">Add One</button>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
    
export default {
    const count = ref(1);
    const doubleCountComputed = computed(() => {
      return count.value * 2;
    });

    const doubleCountMethod = () => {
      return count.value * 2;
    };

    return {
      count,
      doubleCountComputed,
      doubleCountMethod,
    };
    
  },
}
</script>

<style>
</style>
```




