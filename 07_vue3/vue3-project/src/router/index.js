import { createRouter, createWebHistory } from 'vue-router';

import Home from '@/views/Home.vue';
import Todos from '@/views/todos/Index.vue';
import Todo from '@/views/todos/Todo.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    // 객체 하나하나가 1개의 router
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/todos',
      name: 'Todos',
      component: Todos
    },
    {
      path: '/todos/:id', // 동적 router url path (':')
      name: 'Todo',
      component: Todo
    }
  ]
});


export default router;