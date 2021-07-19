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
    {{ greeting(name) }}
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



### 03. Event와 ref

* vue.js composition API를 사용하면 일반 변수를 사용하여 template에 나타내고 있는 값은 나중에 재할당 하여도 template에 적용되지 않음 (변수에는 적용됨)

* 따라서 vue.js에서는 변수값을 재할당 하였을 시,

  - template에도 적용이 되도록하는 ref 기능을 제공

  * 단, 일반 변수에 값을 담으면 안되고 ref를 사용
  * 변수에 값을 담아주기

* 기존 뷰 버전에서는 `ref`가 뷰 템플릿의 DOM 또는 컴포넌트를 가리키는 속성으로 사용되었으나, Vue 3 에서는 `ref`가 `reactive reference`를 의미한다.



* `reactive 하다`
  - data가 변경되면 template에서도 같이 변경되는 것
* `ref`
  - 안에 문자, 숫자, 배열 모두 들어갈 수 있다.

```vue
<template>
  <div class="name">
    <!-- template에서는 name.value로 접근 안해도 됨 -->    
    {{ name }}
  </div>
  
  <!-- v-on 특정 이벤트 발생하면 발생시킬 행위 설정 -->
  <button 
    class="btn btn-primary"
    v-on:click="updateName"
    >
    Click
  </button>
</template>

<script>
// vue에서 ref import 해오기
import { ref } from 'vue';

export default {
  setup() {
    // const name = 'Mini Coder';
    // const는 재할당 불가 하므로 let으로 바꿔주자.
    // let name = 'Mini Coder';
    const name = ref('Mini Coder');

    const updateName = () => {
      // ref를 사용하면 값을 변경할 때 .value를 넣어줘야함
      name.value = 'Cute Mini',
      console.log(name)
    };

    return {
      name,
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
```



- `.value`를 쓰지 않고 재할당 하려면

  - 기본적으로 문자, 숫자는 ref를 사용해야하고
  - object 나 Array는 reactive 사용 가능

  ```vue
  <template>
    <div class="name">
      {{ name }}
    </div>
  
    <button 
      class="btn btn-primary"
      v-on:click="updateName"
      >
      Click
    </button>
  </template>
  
  <script>
  // vue에서 reactive import 해오기
  import { reactive } from 'vue';
  
  export default {
    setup() {
      const name = reactive({
        id: 1
      });
  
      const updateName = () => {
        // name의 .value 사용할 필요 없이
        // name에 id에 바로 접근 가능
        name.id = 2;
          
        // ref를 사용한다면?
        // name.value.id 로 접근해야함
      };
  
      return {
        name,
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
  ```

  

### 04. 데이터 바인딩

> 단방향 바인딩 `v-bind`

```vue
<template>
  <!--<div class="name"> 과 같아짐 -->
  <div v-bind:class="nameClass">
    {{ name }}
  </div>

  <!--input의 원래 있는 속성인 value에 name을 bind시켜주기-->
  <!--모든 속성 bind 가능-->
  <input v-bind:type="test" v-bind:value="name">

  <button 
    class="btn btn-primary"
    v-on:click="updateName"
    >
    Click
  </button>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const name = ref('Mini Coder');
      
    // input type을 숫자형태로 바꾸기
    const test = ref('number');
      
    // nameClass의 값이 name
    // const nameClass = ref('name');
    const nameClass = ref(''); // 처음엔 블랙 => 색 입히고 싶다면

    const updateName = () => {
      name.value = 'Cute Mini';
      // click 버튼 누르면 input type을 숫자에서 text형태로
      test.value = 'text';
      // click 누르면 name 클라스를 먹여서 색깔 입히기
      nameClass.value = 'name';
    };

    return {
      name,
      updateName,
      number,
      nameClass,
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



> 약어

- `v-on:click="updateName"` => `@click="updateName"`
- `v-bind:type="type"` => `:type="type"`



> 양방향 바인딩

- user가 template의 value를 바꿀 시 data도 변경

  - event 활용해서 양방향 바인딩

  ```vue
  <template>
    <!-- oninput Event => user가 input field에 뭔가를 쓸 때 실행 -->
    <input
     type="text"
     :value="name"
     @input="updateName"
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
      
      // input에 user가 뭔가를 써서 value가 바뀌면 updateName 실행
      // 이때 이 함수에서 e(event)라는 객체를 받아옴 
      // => input 박스 자체에 대한 정보를 가지고 있음
      const updateName = (e) => {
        console.log(e)
        name.value = e.target.value;
      };
  
      return {
        name,
        onSubmit,
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
  ```

  

  - `v-model` 로 양방향 바인딩

  ```vue
  <template>
    <!-- v-model로 데이터 연결해주면 함수도 안만들어도 되고 v-on, v-bind 다 필요X -->
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
  ```