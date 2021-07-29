# Vue3_Todo 추가 및 삭제

## Todo Add

### 01. Event Prevent

[https://v3.vuejs.org/guide/events.html#event-modifiers](https://v3.vuejs.org/guide/events.html#event-modifiers ) 

- `v-on` 이벤트에 **이벤트 수식어**를 제공

  - `.prevent`

    이벤트 전파가 중단

  - `.stop`

    이벤트가 페이지를 재로드 안함

  - `.capture`

    이벤트 리스너를 추가할 때 캡처모드를 사용

  - 등등

```vue
<template>
  <div class="container">
    <h2>To-Do List</h2>
    <!-- onsubmit Event -->
    <!-- button의 type을 submit으로 해주면 @click="onsubmit"과 같음 -->
    <!-- click 뿐만 아니라 enter도 인식 -->
    <!-- 이때, 추가될 때 form이 submit이 되면 reloading됨 (form의 특성) -->
    <!-- 그래서 새로고침을 방지하자 => event.preventDefault() -->
    <!-- vue.js에서는 @submit.prevent="onSubmit" 하면 됨 -->
    <form 
      class="d-flex"
      @submit.prevent="onSubmit"
    >
      <div class="flex-grow-1 mr-2">
        <input
          class="form-control"
          type="text"
          v-model="todo"
          placeholder="Type new to-do"
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
    </form>
    <!-- v-for 사용시, key 넣어줘야함 -->
    <!-- unique한 값이 들어가야함 -->
    <!-- key 값은 element 하나하나를 추적하기 위해 사용 -->
    <!-- vue.js2 부터 필수로 사용해줘야함 -->
    <div
     class="card mt-2"
     v-for="todo in todos"
     :key="todo.id"
    >
      <div class="card-body p-2">
        {{ todo.subject }}
      </div>
    </div>
  </div>
  
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    // 처음에 시작할 때 empty string으로 값 주기
    const todo = ref('');
    // 추가된 todo 담아주기
    // 잘 담기는지 확인하기 위해 defalt로 두 개 넣어주기
    const todos = ref([
      {id: 1, subject: '몽이 밥주기'},
      {id: 2, subject: '몽이 목욕시키기'}
    ]);

    const onSubmit = () => {
      // event의 기본적인 refresh하는 속성 예방 (js에서)
      // e.preventDefault();
      // todos에 객체를 추가시키기
      todos.value.push({
        // id는 unique해야 하니까 일단 time을 넣자
        id: Date.now(),
        // todo의 제목
        subject: todo.value
      });
    };
    
    return {
      todo,
      todos,
      onSubmit,
    };
  }  
}
</script>
```



### 02. v-show & v-if

> v-show

- T/F 상관없이 항상 렌더링 되고 DOM에 남아있다.
- False인 경우, style을 이용해서 감추는 것
- 초기 렌더링 하는 데 비용이 많이 든다.

```vue
<template>
  <!-- toggle이 ture면 보여줘라 -->
  <div v-show="toggle">true</div>
  <!-- toggle이 flase면 보여줘라 -->
  <div v-show="!toggle">false</div>
  <!-- Toggle을 클릭했을때 onToggle이라는 함수 실행 -->
  <button @click="onToggle">Toggle</button>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const toggle = ref(false);
      
    const onToggle = () => {
      // toggle value를 반대로 바꾸기 (클릭할때마다)
      toggle.value = !toggle.value;    
    };

    return {
      toggle,
      onToggle,
    };
    
  },
}
</script>
```



> v-if

- 애초에 조건에 만족하는 것만 (True일 때만) 렌더링!
- Toggle하는 데 비용이 많이 든다.

```vue
<template>
  <div v-if="toggle">true</div>
  <div v-else>false</div>
  <button @click="onToggle">Toggle</button>
  <div class="container">
    <h2>Todo List</h2>
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
    <!-- input에 빈 값 일때, enter나 click해서 add 하려 하면 error 뜨게 하기-->
    <!-- todo 추가를 자주 사용하니까 v-if보다 v-show를 사용 -->
    <div v-show="hasError" style="color:red">Error! This field cannot be empty</div>
    </form>
    <div
     class="card mt-2"
     v-for="todo in todos"
     :key="todo.id"
    >
      <div class="card-body p-2">
        {{ todo.subject }}
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const toggle = ref(false);
    const todo = ref('');
    const todos = ref([
      {id: 1, subject: '몽이 밥주기'},
      {id: 2, subject: '몽이 목욕시키기'}
    ]);

    const hasError = ref(false);

    const onSubmit = () => {
      // todo 가 빈값이면 hasError를 T로 아니면 Todos에 추가해주기
      if (todo.value === '') {
        hasError.value = true;
      } else {
        todos.value.push({
          id: Date.now(),
          subject: todo.value
        });
        // todos에 추가해주고 나서 hasError 메세지는 없어야 하니까 F로
        hasError.value = false;
      }      
    };

    const onToggle = () => {
      toggle.value = !toggle.value;    
    };    

    return {
      todo,
      todos,
      toggle,
      hasError,
      onSubmit,
      onToggle,
    };
    
  },
}
</script>
```



### 03. Input CheckBox

```vue
<template>
            
  <!-- checkbox -->
  <div class="form-check">
    <input
     class="form-check-input"
     type="checkbox"
     v-bind="todo.completed"
    >
  	<label class="form-check-label">{{ todo.subject }}</label>
  </div>  
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const todo = ref('');
    const todos = ref([
      // 초기값 없는 상태로 시작
      // {id: 1, subject: '몽이 밥주기'},
      // {id: 2, subject: '몽이 목욕시키기'}
    ]);

    const hasError = ref(false);

    const onSubmit = () => {
      if (todo.value === '') {
        hasError.value = true;
      } else {
        todos.value.push({
          id: Date.now(),
          subject: todo.value,
          // todo의 완료 여부 (초기값은 당연히 미완료)
          completed: false,
        });
        hasError.value = false;
        // input에 입력되었던 값 지우기
        todo.value = '';
      }      
    };

    return {
      todo,
      todos,
      hasError,
      onSubmit,
    };
    
  },
}
</script>
```



### 04. Class / Style 바인딩

- Style 바인딩

```vue
<template>
  <div class="card-body p-2">
    <div class="form-check">
      <input
       class="form-check-input"
       type="checkbox"
       v-model="todo.completed"
      >
      <!-- todo의 text 부분 -->
      <!-- todo가 completed면 todoStyle적용해서 선 긋고 아니면 빈 obj로 주어주기 -->
      <label
        class="form-check-label"
        :style="todo.completed ? todoStyle : {}"
       >
        {{ todo.subject }}
      </label>
    </div>          
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const toggle = ref(false);
    const todo = ref('');
    const todos = ref([]);
    const hasError = ref(false);
      
    // style은 변경 될 일 없으니까 ref로 안해도 됨
    const todoStyle = {
      // css에서는 text-decoration 지금은 js
      textDecoration: 'line-through',
      color: 'gray'
    };

    const onSubmit = () => {
      if (todo.value === '') {
        hasError.value = true;
      } else {
        todos.value.push({
          id: Date.now(),
          subject: todo.value,
          completed: false,
        });
        hasError.value = false;
        todo.value = '';
      }      
    }; 

    return {
      todo,
      todos,
      toggle,
      hasError,
      todoStyle,
      onSubmit,
    };
    
  },
}
</script>
```



- Class 바인딩

```vue
<template>
  <div class="card-body p-2">
    <div class="form-check">
      <input
       class="form-check-input"
       type="checkbox"
       v-model="todo.completed"
      >
      <!-- Class 바인딩 중 Object Syntax -->
      <!-- object안에 key값으로 넣고 싶은 class name
      	value에 Boolean 들어감
      	value가 T면 key값인 class가 추가/ F면 추가 안됨 -->
      <label
       class="form-check-label"
       :class="{ todo: todo.completed }"
      >
       {{ todo.subject }}
      </label>
    </div>          
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const toggle = ref(false);
    const todo = ref('');
    const todos = ref([]);
    const hasError = ref(false);

    const onSubmit = () => {
      if (todo.value === '') {
        hasError.value = true;
      } else {
        todos.value.push({
          id: Date.now(),
          subject: todo.value,
          completed: false,
        });
        hasError.value = false;
        todo.value = '';
      }      
    };

    return {
      todo,
      todos,
      toggle,
      hasError,
      onSubmit,
    };
    
  },
}
</script>

<style>
  .todo {
    color: gray;
    text-decoration: line-through;
  }
</style>
```



## Todo Delete

```vue
<template>
      <!-- Todo가 없을 때만 이 멘트 작성 -->
      <div v-if="!todos.length">
        추가된 Todo가 없습니다.
      </div>
      <!-- v-for 할 때 두번째 인자로 index 사용 가능 -->
      <div
      class="card mt-2"
      v-for="(todo, index) in todos"
      :key="todo.id"
      >
        <div class="card-body p-2 d-flex align-items-center">
          <div class="form-check flex-grow-1">
            <input
             class="form-check-input"
             type="checkbox"
             v-model="todo.completed"
            >
            <label
             class="form-check-label"
             :class="{ todo: todo.completed }"
            >
             {{ todo.subject }}
            </label>
          </div>
          <div>
            <!-- btn 누르면 Todo 삭제 -->
            <button
             class="btn btn-danger btn-sm"
             @click="deleteTodo(index)"
            >
              Delete
            </button>
          </div>          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const toggle = ref(false);
    const todo = ref('');
    const todos = ref([]);
    const hasError = ref(false);

    const onSubmit = () => {
      if (todo.value === '') {
        hasError.value = true;
      } else {
        todos.value.push({
          id: Date.now(),
          subject: todo.value,
          completed: false,
        });
        hasError.value = false;
        todo.value = '';
      }      
    };

    const deleteTodo = (index) => {
      // console.log('delete todo')
      // todos의 특정 todo를 한개 지우자
      todos.value.splice(index, 1)
    };

    return {
      todo,
      todos,
      toggle,
      onSubmit,
      deleteTodo
    };
    
  },
}
</script>

<style>
  .todo {
    color: gray;
    text-decoration: line-through;
  }
</style>
```



-----

✍`Todo 추가 생성 삭제 코드`

```vue
<template>
  <div>
    <div v-if="toggle">true</div>
    <div v-else>false</div>
    <button @click="onToggle">Toggle</button>
    <div class="container">
      <h2>Todo List</h2>
      <TodoSimpleForm/>
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
      <div v-if="!todos.length">
        추가된 Todo가 없습니다.
      </div>
      <div
      class="card mt-2"
      v-for="(todo, index) in todos"
      :key="todo.id"
      >
        <div class="card-body p-2 d-flex align-items-center">
          <div class="form-check flex-grow-1">
            <input
             class="form-check-input"
             type="checkbox"
             v-model="todo.completed"
            >
            <label
             class="form-check-label"
             :class="{ todo: todo.completed }"
            >
             {{ todo.subject }}
            </label>
          </div>
          <div>
            <button
             class="btn btn-danger btn-sm"
             @click="deleteTodo(index)"
            >
              Delete
            </button>
          </div>          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import TodoSimpleForm from './components/TodoSimpleForm.vue'

export default {
  components: {
    TodoSimpleForm
  },
  setup() {
    const toggle = ref(false);
    const todo = ref('');
    const todos = ref([]);
    const hasError = ref(false);

    const todoStyle = {
      textDecoration: 'line-through',
      color: 'gray'
    };

    const onSubmit = () => {
      if (todo.value === '') {
        hasError.value = true;
      } else {
        todos.value.push({
          id: Date.now(),
          subject: todo.value,
          completed: false,
        });
        hasError.value = false;
        todo.value = '';
      }      
    };

    const onToggle = () => {
      toggle.value = !toggle.value;    
    };    

    const deleteTodo = (index) => {
      todos.value.splice(index, 1)
    };

    return {
      todo,
      todos,
      toggle,
      hasError,
      todoStyle,
      onSubmit,
      onToggle,
      deleteTodo
    };
    
  },
}
</script>

<style>
  .todo {
    color: gray;
    text-decoration: line-through;
  }
</style>
```



