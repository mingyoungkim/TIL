# Vue3_Todo Form

## Todo 추가 폼 만들기

### 01. Vue 컴포넌트

> Component란?

* 하나의 부품(component)
* component파일을 만들면 확장자가 vue가 된다.



> 구성

- vue component는 세 부분으로 나눠진다.

  1. template
     - html 코드가 들어간다.

  2. script
     - 자바스크립트 로직이 들어간다

  3. style
     - CSS 코드가 들어간다



> Vue3 로 오면서 변한 점

- composition API란?
  - 구성 요소 논리를 유연하게 구성할 수 있는 추가 기능 기반 API

  - Vue 3.0 에서 새로 추가된 함수 기반의 API

  - 목적

    - 기존에 사용하던 Options API를 사용해서 논리구조를 분리
    - 재사용을 가능

    ```text
    기존에도 mixin 기능을 활용하면 코드를 재사용 할 수 있었지만, 
    오버라이딩 문제나 여러가지 mixin을 상속받을 경우 컴포넌트를 관리하기가 조금 까다로워지는 등 아쉬움이 있어 이러한 단점을 보완하기 위해 Composition API를 사용한다.
    ```

- template
  - template에 큰 <div></div>로 감싸주고 여러 개의 태그를 넣어야했다.

  - But now,

    큰 <div></div> 가 없어도 여러 개의 태그를 그냥 넣어도 가능



### 02. 함수 사용

```vue
<template>
  <!-- 1. -->
  <div>Mini Coder</div>

  <!-- 2. -->
  <div class="name">
    <!-- 함수는 괄호 불러서 호출해야함 -->
    {{ greeting(name)}}
  </div>

  <!-- 3. -->
  <div>{{ greet }}</div>
</template>

<script>
export default {
  setup() {
    // 1.
    // 필요한 로직 작성
    const name = 'Mini Coder';
	
    // 2.
    // greeting이라는 변수에 함수를 넣는 로직
    // greeting 함수에 callname이라는 매개변수를 넣어서 함수안에서 그 매개변수를 사용 가능
    const greeting = (callname) => {
      return 'Hello '+ callname;
    };
	
    // 3.
    // name과 greeting 함수를 한번에 greet에 넣어서 return해서 나타낼 수도 있다.
    const greet = greeting(name);

    // return 해주면 template에서 사용 가능
    return {
      name,
      greeting,
      greet,
    };
  }  
}
</script>

<style>
  .name {
    color: violet
  }
</style>
```



### 03. Event

