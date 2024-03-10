<!-- vue 라고 치면 vue section 자동 완성 -->
<template>
  <div
    v-for="(todo, idx) in todoList"
    :key="todo.id"
    class="card mt-2"
  >
    <div class="card-body p-2 d-flex align-items-center">
      <div class="form-check flex-grow-1">

        <!-- 자식 컴포넌트에서 props로 받은 데이터를 직접적으로 변경하면 안되기 때문에 -->
        <!-- v-model 사용 불가 -> value 바인딩으로 변경 -->
        <!-- <input type="checkbox" class="form-check-input" v-model="todo.completed"> -->
        <input 
          type="checkbox" 
          class="form-check-input" 
          :value="todo.completed"
          @change="toggleTodo(idx)"
        >

        <label 
          class="form-check-label" 
          :style="todo.completed ? todoListtyle : {}" 
          :class="{ todo : !todo.completed }">
          {{ todo.subject }}
        </label>
      </div>
      <div>
        <button class="btn btn-danger btn-sm" @click="deleteTodo(idx)">
          Delete
        </button>
      </div>
    </div>
  </div>
  
</template>

<script>
export default {
  // 부모컴포넌트에서 정의한 이름으로 내려준 데이터 받기 (template에서 해당 이름으로 사용 가능)
    // 1. props의 이름만 넣는 방법
  // props : ['todoList'],
    // 2. props를 object 로 받아보기
    // 받는 type 지정 가능
    // required 설정 가능 : 해당 컴포넌트에서는 항상 todoList가 반드시 필요함
  // 주의사항
    // props 는 'one-way-data-flow' : 모든 props는 부모에서 자식으로만 데이터를 내려줄 수 있다.
    // so, 부모컴포넌트에서 property가 변경되면 자식컴포넌트에서 받은 props 데이터도 바뀜 (반대는 x : 자식에서 해당 데이터를 직접적으로 변경하면 안된다)
  props: {
    todoList: {
      type: Array,
      required: true,
    }
  },

  // 자식컴포넌트에서 부모컴포넌트로 이벤트 보내기 : emit 
  // vue3 에서부터 상단 props 처럼 emit 도 등록하도록 권장
    // 해당 컴포넌트에서 어떠한 emit 이벤트를 사용하는지 한눈에 파악 가능
  emits: ['toggle-todo', 'delete-todo'],

  // setup(props, context) {
  //   const toggleTodo = (index) => {
  //     context.emit('toggle-todo', index);
  //   };

  //   const deleteTodo = (index) => {
  //     context.emit('delete-todo', index);
  //   };

  //   return {
  //     toggleTodo,
  //     deleteTodo,
  //   }
  // }
  
  // context 반복 제거
    // context는 객체를 보내주는데, 그 안에 emit을 빼오면 됨
  setup(props, { emit }) {
    const toggleTodo = (index) => {
      emit('toggle-todo', index);
    };

    const deleteTodo = (index) => {
      emit('delete-todo', index);
    };

    return {
      toggleTodo,
      deleteTodo,
    }
  }
}
</script>
