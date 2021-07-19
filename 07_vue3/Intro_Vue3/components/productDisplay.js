// 첫번째 인자는 component 이름
// 두번째 인자는 object to configure our component
app.component('product-display', {
  // a custom attribute for passing data into a component
  props: {
    premium:{
      // prop validation
      type: Boolean,
      required: true,
    }
  },
  // template property
  template:
  // 백틱 + /*html*/ 해서 가져오기 => es6-string-html 에 의해 가능
  /*html*/
  `<div class="product-display">
    <div class="product-container">
      <div class="product-image">
        <!-- image goes here -->

        <!-- v-bind -->
        <!-- 2. attribute = src / expression = "image" => 이 두가지를 v-bind로 bond -->
        <!-- 현재 js 쓰고 있어서 class명 등 Camel로 써야하는데 Kebap 케이스로 쓰고 싶으면 '' 에 작성 -->
        <img v-bind:src="image" :class="{ 'out-of-stock-img' : !inStock }">
        <!-- <img :src="image" alt=""> // 약어--> 
      </div>

      <div class="product-info">
        <!-- <h1>Product goes here</h1> -->
        <!-- 1. data에 담긴 정보 사용 -->
        <!-- <h1>{{ brand + ' ' + product }}</h1> --> <!--데이터를 같이 쓰려고할 때, 이렇게 쓰면 길어짐 => computed를 쓰자-->
        <h1>{{ title }}</h1>
        <h2 v-if="onSale">{{ Sale }}</h2>
        <p>{{ description }}</p>
        <a :href="url">Google</a>

        <!-- 3. v-if -->
        <p v-if="inventory > 10">In Stock</p>            
        <p v-else-if="inventory <= 10 && inventory > 0">Almost SoldOut!</p> <!-- && : and -->
        <p v-else>Out of Stock</p>
        <!-- v-show는 항상 렌더링은 하지만 보이지 않게 스타일처리 -->
        <!-- <p v-show="inventory > 10">In Stock</p> -->
        <p v-if="onSale">On Sale!</p>

        <p>Shipping {{ shipping }}</p>

        <!-- 4. v-for -->
        <ul>          
          <p>Detail</p>
          <!-- <li v-for="detail in details">{{ detail }}</li> -->

          <product-details :details="details"></product-details> 
          
          <p>Size</p> 
          <li v-for="(size, index) in sizes" :key="index">{{ size }}</li>            
        </ul>
        <!-- v-for 에서 key는 각각의 요소의 unique한 값? 부여해주는 것 (index느낌) -->
        <!-- <div 
          v-for="variant in variants" 
          :key="variant.id" 
          @mouseover="changeImg(variant.image)"
          class="color-circle"
          :style="{ backgroundColor: variant.color }">
          {{ variant.shape }}
        </div> -->

        <!-- 남자, 여자 양말 수량에 따라 바꾸기 -->
        <div 
          v-for="(variant, index) in variants" 
          :key="variant.id" 
          @mouseover="updateVariant(index)"
          class="color-circle"
          :style="{ backgroundColor: variant.color }">
          {{ variant.shape }}
        </div>

        <!-- 5. v-on -->
        <!-- v-on:이벤트종류="그 이벤트가 일어난 경우, 발생할 행위" -->
        <!-- <div class="button" v-on:click="cart += 1">Add to Cart</div> -->
        <!-- 이때 행위에 대한 로직이 길어지는 것을 대비해서 method로 정의하고 가져오기 -->
        <button
        class="button"
        :disabled="!inStock"
        @click="addToCart"               
        :class="{ disabledButton: !inStock }">
        Add to Cart
        </button>
        <button class="button" @click="delFromCart">Delete from Cart</button>
      </div>
    </div>
  </div>`,
  // main.js에 있던 애들
  data() {
    return {
      // cart: 0,
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
    },
    shipping() {
      if (this.premium) {
        return 'Free'
      }
      return 2.99
    }
  }
}
) 