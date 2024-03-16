<template>
  <!---------- 8. vue Router ---------->
  <!-- nav bar 추가 -->
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <!-- a태그의 href : 페이지 이동 => vue 에서 페이지 이동은 지양 (다운받았던 것을 다시 다운받게됨) -->
    <!-- <a class="navbar-brand" href="/">Mini Home</a> -->
    <router-link class="navbar-brand" to="/">
      Mini Home
    </router-link>
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <!-- <a class="nav-link" href="/todos">Todos</a> -->
        <router-link class="nav-link" to="/todos">
          Todos
        </router-link>
      </li>
    </ul>
  </nav>
  
  <div class="container">
    <!-- router-view 넣어주면, 페이지를 이동할때마다 router-view에 homeComponet 가 들어가게됨 -->
    <router-view/>
  </div>
  

</template>


<script>
</script>

<style>

</style>