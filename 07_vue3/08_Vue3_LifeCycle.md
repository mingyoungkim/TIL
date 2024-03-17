# Vue3_LifeCycle_Composables

## Life Cycle
> 생명주기

### 실행 순서

```vue
  <script>
    import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted } from 'vue';
    
    /* console 순서
      1. setup 바로 안의 log
        : setup 함수가 코드를 먼저 쭉 읽기 때문에 해당 console 먼저 찍히고 onBeforeMount가 실행
      2. onBeforeMount
      3. onMounted
        : mount 된 후에 마지막에 실행
      4. onBeforeUpdate
        : setup 안의 state 가 바뀌기전 실행
      5. onUpdated
        : setup 안의 state 가 update 된 후 실행
      6. onBeforeUnmount
      7. onUnmounted
    */

    export default {
      setup() {
        /* onBeforeMount
          dom 에 mount 가 되기 전에 실행되는 함수
          아직 mount 안되었기 때문에 template의 태그에 접근 불가
        */
        onBeforeMount(() => {
          console.log(document.querySelector('#page-header')); // null
        });
        // dom 에 mount 가 되었을 때 실행
        onMounted(() => {
          console.log(document.querySelector('#page-header')); // 출력 O
        });

        // setup 안의 state (에시: todo) 를 update 하면서 update 되기 전에 onBeforeUpdate 가 실행
        onBeforeUpdate(() => {
          console.log('before update');
        });
        // update 된 후 실행
        onUpdated(() => {
          console.log('updated');
        });

        // 해당 컴포넌트에서 다른 페이지로 이동하게 되면 unMount 실행
        // 해당 컴포넌트에서 unmount(빠져나가기) 전에 메모리 누수를 방지하기 위해 쓸데없는 애들을 메모리에서 정리하기 위해 사용
        onBeforeUnmount(() => {
          console.log('before unmonnt');
        });
        onUnmounted(() => {
          console.log('unMounted');
        });

        console.log('1. 제일번저 찍힐 걸?'); 
      }
    }
  </script>
```

## Composables
> 상태를 가진 로직을 캡슐화하고 재활용할 수 있게 Composition API를 이용하는 함수

- 다른 js 파일에다가 함수를 만들고 이 함수를 컴포넌트에 가져와서 사용