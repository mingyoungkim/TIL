# Vue3_Components

## 자식 컴포넌트 생성

### 01. 자식 컴포넌트 Import해서 출력시키기

- 하위 컴포넌트 생성

  ```vue
  <template>
    <h2>Todo Simple Form</h2>
  </template>
  
  <script>
  // component는 하나의 부품이라서 다른 곳에서 가져다 쓸 수 있음
  // TodoSimpleForm을 App.vue에서 불러서 사용하는 것을 구현해보자.
  export default {
    setup() {
      
    },
  }
  </script>
  
  <style>
  
  </style>
  ```



- 부모 컴포넌트에 작업

  1. Import 해오기
  2. Import한 component 등록

  ```vue
  <script>
  import { ref } from 'vue';
  // 1. TodoSimpleForm 가져다쓰기 위해 import
  import TodoSimpleForm from './components/TodoSimpleForm.vue'
  
  export default {
    // 2. import한 component를 등록하기
    // 등록하면 이제 이 component를 App.vue에서 사용가능해짐
    components: {
      TodoSimpleForm
    
    },
    setup() {
      
    },
  }
  </script>
  ```

  3. template에 보여주기

  ```vue
  <template>
    <!-- 3. tag처럼 template에 적어주면 화면에 출력됨 -->
    <TodoSimpleForm/>      
  </template>
  ```



### 02. Emit & Props

> Emit

- Emit을 통해 자식 컴포넌트에서 부모 컴포넌트로 데이터 보내기

  - 자식 컴포넌트

  ```vue
  <template>
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
    
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    // Vue3에서 달라진점!! => 한눈에 보기 쉽게 보낼 emits들을 위에 작성해주기
    emits: ['add-todo'],
    // 1. 두 개의 인자 받기 (props, context object)
    // context -> 자식 컴포넌트에서 부모컴포넌트로 데이터 보낼때 필요한 것이 context 안에 있음
    // context안에 emit이라는 함수가 들어있음
    setup(props, context) {
      const todo = ref('');
      const hasError = ref(false);
  
      const onSubmit = () => {
        if (todo.value === '') {
          hasError.value = true;
        } else {
          // 2. todos Array에 todo 추가 시키는 로직을 부모 컴포넌트로 올려주기
          // emit 함수를 통해 부모 컴포넌트로 'add-todo'라는 이벤트를 보냄
          // 두번째 인자로 올려주고 싶은 데이터 적기
          // onSubmit 함수가 실행되면 부모 컴포넌트로 'add-todo'로 데이터를 보내주게 됨
          context.emit('add-todo', {
            id: Date.now(),
            subject: todo.value,
            completed: false,
          })        
          // todos.value.push({
          //   id: Date.now(),
          //   subject: todo.value,
          //   completed: false,
          // });
          hasError.value = false;
          todo.value = '';
        }      
      };
  
      return {
        todo,
        hasError,
        onSubmit,
      };
      
    },
  }
  </script>
  
  <style>
  
  </style>
  ```

  - 부모 컴포넌트
  
  ```vue
  <template>
    <div>
      <div class="container">
        <h2>Todo List</h2>
          
        <!--3. 보여줄 자식 컴포넌트에 emit을 통해 받아온 이벤트 연결 (이벤트니까 v-on)-->
        <TodoSimpleForm @add-todo="addTodo"/>
        
        <!-- Form 부분을 자식 컴포넌트에 넣어주기~ -->
        <!-- <form @submit.prevent="onSubmit">
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
        </form> -->
          
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
      
      const todos = ref([]);
      
  
      const todoStyle = {
        textDecoration: 'line-through',
        color: 'gray'
      };
  
      // const onSubmit = () => {
      //   if (todo.value === '') {
      //     hasError.value = true;
      //   } else {
      //     todos.value.push({
      //       id: Date.now(),
      //       subject: todo.value,
      //       completed: false,
      //     });
      //     hasError.value = false;
      //     todo.value = '';
      //   }      
      // };
  	
      // 4. template에서 이 함수가 시작될때 자식 컴포넌트에서 받은데이터 인자로 받음
      const addTodo = (todo) => {
        // console.log(todo);
        todos.value.push(todo)
      };
  
      const onToggle = () => {
        toggle.value = !toggle.value;    
      };    
  
      const deleteTodo = (index) => {
        todos.value.splice(index, 1)
      };
  
      return {
        todos,
        todoStyle,
        deleteTodo,
        addTodo
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



> Props

- Props 사용시 주의점

  - 부모에서 자식으로만 데이터 보내주는 역할 `one-way-down bindind`

  - 부모 컴포넌트의 property가 변경되면 props로 받은 데이터도 자식 컴포넌트에서 같이 변경

    (그 반대는 ❌)
  
- Props를 통해 부모 컴포넌트에서 자식 컴포넌트로 데이터 보내기

  [https://v3.vuejs.org/guide/component-props.html](https://v3.vuejs.org/guide/component-props.html ) 

  - 부모 컴포넌트

  ```vue
  <template>
    <div>
      <div class="container">
        <h2>Todo List</h2>
  
        <TodoSimpleForm @add-todo="addTodo"/>
        
        <div v-if="!todos.length">
          추가된 Todo가 없습니다.
        </div>
  
        <!-- 3. 보여주기 -->
        <!--4. 자식 컴포넌트로 보낼 todos데이터를 todoList라는 이름으로 보내주기-->
        <!-- 자식 컴포넌트에서 보내준 toggle-todo 이벤트 연결 -->
        <TodoList :todoList="todos" @toggle-todo="toggleTodo"/>
  
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue'
  import TodoSimpleForm from './components/TodoSimpleForm.vue'
  // 1. import 해오기
  import TodoList from './components/TodoList.vue'
  
  export default {
    components: {
      TodoSimpleForm,
      // 2. 등록
      TodoList
    },
    setup() {
      const toggle = ref(false);
      
      const todos = ref([]);
      
  
      const todoStyle = {
        textDecoration: 'line-through',
        color: 'gray'
      };
  
  
      const addTodo = (todo) => {
        todos.value.push(todo)
      };
  
      const onToggle = () => {
        toggle.value = !toggle.value;    
      };    
  
      const deleteTodo = (index) => {
        todos.value.splice(index, 1)
      };
  
      const toggleTodo = (index) => {
        // console.log(todos.value[index]);
        todos.value[index].completed = !todos.value[index].completed;
        // console.log(todos.value[index]);
      };
  
      return {
        todos,
        todoStyle,
        deleteTodo,
        addTodo,
        toggleTodo
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
  
  - 자식 컴포넌트
  
  ```vue
  <template>
    <div
      class="card mt-2"
      v-for="(todo, index) in todoList"
      :key="todo.id"
    >
      <div class="card-body p-2 d-flex align-items-center">
        <div class="form-check flex-grow-1">
          <!-- v-model을 사용하면 양방향 바인딩으로 자식컴포넌트에서 데이터를 변경하게됨 -->
          <!-- props는 부모에서 변경된 데이터만 자식으로 전달되니까 
            자식컴포넌트에서 데이터를 변경해도 부모 컴포넌트로 전달이 안됨 -->
          <!--So, 단일 binding 쓰자-->
          <!-- <input class="form-check-input" type="checkbox" v-model="todo.completed"> -->
          <input
            class="form-check-input"
            type="checkbox"
            :value="todo.completed"
            @change="toggleTodo(index)"
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
    
  </template>
  
  <script>
  export default {
    // 5. 받아온 데이터 정해진 이름대로 받기
    // 이제 template에서 todos 데이터 접근가능
    // props: ['todoList']
  
    // object로 데려올 수도 있음
    props: {
      todoList: {
        type: Array,
        required: true
      }
    },
    emits : ['toggle-todo', 'delete-todo'],
    setup(props, context) {
      const toggleTodo = (index) => {
        context.emit('toggle-todo', index);
  
      };
    return {
      toggleTodo
    };
    }
     
  
  }
  </script>
  
  <style>
  
  </style>
  ```
  
  
  
  - context 를 반복적으로 사용하는 것의 번거로움 해결하기
  
  ```text
  setup(props, context) {
      const toggleTodo = (index) => {
        context.emit('toggle-todo', index);
  
      };
    return {
      toggleTodo
    };
    
  ----------------------------------------------------------------------------------------------------
  
  //  객체 구조 분해를 통해서 context에서 emit만 빼오기
  setup(props, { emit }) {
      const toggleTodo = (index) => {
        emit('toggle-todo', index);
      };
  
      const deleteTodo = (index) => {
        emit('delete-todo', index);
      };
  ```
