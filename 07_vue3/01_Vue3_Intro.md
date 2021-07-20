# Vue3_Intro

## 설치부터 프로젝트 구경까지

### 01. 설치 단계

[설치환경]: https://kr.vuejs.org/v2/guide/installation.html



1. node.js 설치

   - npm 및 yarn을 사용하기 위해

   - `node -v`

     `npm -v`

2. vue.js 설치

3. vue.cli 설치

   - `npm install -g @vue/cli`
   - `vue -V`

4. vue프로젝트 설치

   - `vue create 프로젝트 명`
   - 2번째 항목 선택

5. 확장 프로그램 Vetur 설치 및 세팅

   - 프로젝트 최상위에 jsconfig.json 파일 만들고

   - Vetur 프로젝트 setup 넣어주기

     ```json
       {
         "include": [
           "./src/**/*"
         ]
       }
     ```

     

### 02. 폴더 구조 파악

* `package.json`

  * `dependencies`, `devDependencies`
    * 필요한 패키지들을 리스트로 저장해놓는 공간
      * 패키지란? 쉽게 말하자면 남들이 만들어 놓은 부품
      * 따라서 개발을 할 때 이 패키지들을 사용하기 위해서 `dependencies`와 `devDependencies`에 리스트로 저장
      * `dependencies` : 개발을 할때, production에 올릴때 필요한 패키지들을 담아놓은곳
      * `devDependencies` : 개발을 하는 동안에만 유용한 패키지들을 담아놓는 곳(나중에 production에 올릴때에는 이 패키지들은 필요하지 않다.). 또한 설치를 하게 되면 `node_modules` 안에 폴더형태로 설치
        * Q: 그러면 왜 node_modules 안에 막상 들어가보면 패키지들이 수백개가 설치되어 있나요?
        * A: 하나의 패키지 안에서 내부적으로 사용하는 패키지들까지 같이 설치가 되기 때문

* `public`

  * `index.html`

    * vue프로젝트를 웹 브라우저에서 열었을 때 처음으로 받아오는 html파일

    * ```html
      <!DOCTYPE html>
      <html lang="">
        <head>
          <meta charset="utf-8">
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <meta name="viewport" content="width=device-width,initial-scale=1.0">
          <link rel="icon" href="<%= BASE_URL %>favicon.ico">
          <title><%= htmlWebpackPlugin.options.title %></title>
        </head>
        <body>
          <noscript>
            <strong>We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
          </noscript>
          <div id="app"></div>
          <!-- built files will be auto injected -->
        </body>
      </html>
      
      ```

    * 위의 코드를 보면 id="app"인 div 태그가 하나 있는데 이 태그안에서 vue application이 전부 구동이 된다.

    * 나중에 build를 하게 되면 div태그 밑줄에 자바스크립트 script가 자동으로 들어가게된다.

      * 자바스크립트 script가 들어가게 되면 src(source) 폴더 내에 있는 main.js가 가장먼저 실행된다.

      * main.js

        * ```js
          // vue에서 createApp 함수를 가져와서
          import { createApp } from 'vue'
          import App from './App.vue'
          // vue3가 되면서 기존의 Vue 생성자 함수를 사용하는 대신에, createApp() 함수를 사용한다.
          // 최상위 컴포넌트(App)를 createApp 함수에 넣어주고
          // App 컴포넌트의 컨텐츠를 id가 app인 div태그안에 넣는다.
          createApp(App).mount('#app')
          ```

      * App.vue 컴포넌트

        ```vue
        <template>
          <!-- 이미지 태그가 있다. -->
          <img alt="Vue logo" src="./assets/logo.png">
          <!-- 3. HelloWorld 태그에서 메세지를 띄운다. -->
          <HelloWorld msg="Welcome to Your Vue.js App"/>
        </template>
        
        <script>
        // 1. HelloWorld.vue로부터 HelloWorld를 불러와서
        import HelloWorld from './components/HelloWorld.vue'
        
        export default {
          // 2. 이름이 App인 컴포넌트에 HelloWorld 컴포넌트를 등록한다.
          name: 'App',
          components: {
            HelloWorld
          }
        }
        </script>
        
        <style>
        #app {
          font-family: Avenir, Helvetica, Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
          text-align: center;
          color: #2c3e50;
          margin-top: 60px;
        }
        </style>
        ```

        * image 태그가 id가 App인 div 태그안에 잘 들어갔는지 웹 브라우저에서 확인해보자.

          * package.json파일을 살펴보면 다음과 같은 코드가 있을 것이다.

            ```json
              "scripts": {
                "serve": "vue-cli-service serve",
                // build는 production에 올리기 전에 production에 올리기에 최적화 된 파일을 만드는 과정이다.
                "build": "vue-cli-service build",
                "lint": "vue-cli-service lint"
              },
            ```

            이 말인 즉슨, 개발서버를 실행시키기 위해서는 "serve"를 사용해야 한다는 것이다.

            터미널에서 `npm run serve` 명령어로 개발서버를 실행시킬수 있다.




### 03. 실행

```bash
$ cd vue3-project
$ npm run serve
```

