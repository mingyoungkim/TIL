const app = Vue.createApp({
  // 다른 곳에 데이터를 보내줄라고 여기다 저장
  // data: function() { // 이거를 줄일 수 있음
  data() {
    return {
      cart: 0,
      // premium user냐 아니냐
      premium: false,
    }
  },
  methods: {
  },
})