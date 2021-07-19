const app = Vue.createApp({
  // 다른 곳에 데이터를 보내줄라고 여기다 저장
  // data: function() { // 이거를 줄일 수 있음
  data() {
    return {
      cart: 0,
      product: 'Socks',
      brand: 'mini',
      description: 'This is my favorite Socks',
      // image: './assets/images/img1.jpg', // computed로 해보기
      seletedVariant: 0,
      url: 'https://www.google.com/',
      inventory: 0,
      // inStock: false, // computed로 해보기
      onSale: false,
      details: ['50% cotton', '30% wool', '20% polyester'],
      variants: [
        { id: 2234, shape: 'man', image: './assets/images/img1.jpg', color: 'blue', quantity: 0 },
        { id: 2235, shape: 'woman', image: './assets/images/img2.jpg', color: 'pink', quantity: 50 },
      ],
      sizes: [230, 275, 280],
    }
  },
  methods: {
    addToCart() {
      // this => data안
      this.cart += 1     
    },
    delFromCart() {
      if (this.cart >= 1) {
      this.cart -= 1
      }
    },
    changeImg(varientImage) {
      this.image = varientImage
    },
    updateVariant(index) {
      this.seletedVariant = index
      // console.log(index)
    }
  },
  // computed를 계산기라고 생각하자
  computed: {
    title() {
      return this.brand + ' ' + this.product
    },
    Sale() {
      if (this.onSale) {
        return this.brand + ' ' + this.product + ' is on Sale!'
      }
      return ''
    },
    image() {
      return this.variants[this.seletedVariant].image
    },
    inStock() {
      return this.variants[this.seletedVariant].quantity
    }
  }
})