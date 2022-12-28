<script setup>
import Scan from './components/Scan.vue'
</script>

<script>
  export default {
    components: {
      Scan
    },
    data() {
      return {
        scanningOn: false,
      }
    },
    methods: {
      scanToggle(){
        this.scanningOn = !this.scanningOn
      }
    }
}

</script>

<template>
  <header>
    <!--
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />
    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
    -->

  </header>

  <main>
    <!-- TheWelcome /-->
    
    <!-- Header -->
    <div class="container">
      <header class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">
        <a href="/" class="d-flex align-items-center col-md-3 mb-2 mb-md-0 text-dark text-decoration-none">
          <object data="/src/assets/plant-lib-logo.svg" class="bi me-2" width="333" height="48"></object>
        </a>
        <div class="col-md-3 text-end">
          <button type="button" class="btn btn-outline-dark me-2">Login</button>
        </div>
      </header>
    </div>

    <div class="container text-center" style="height: 650px;">

      <Scan :scanning="scanningOn" />

    </div>

    <!-- Buttons -->
    <div class="container py-4 text-center" >
      <div class="d-grid gap-2 d-md-flex justify-content-md-center">
        <button class="btn btn-lg px-4 btn-success" type="button" @click="scanToggle">Scan</button>
        <button class="btn btn-lg px-4 btn-outline-dark" type="button">Plants</button>
        <button class="btn btn-lg px-4 btn-outline-dark" type="button">Labels</button>
      </div>
    </div>

    <!-- Footer -->
    <div class="container">
      <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
        <p class="col-md-4 mb-0 text-muted">© 2022 Dmitry Natkha</p>
        <a href="/" class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
          <object data="/src/assets/plant-lib-logo-small.svg" class="bi me-2" width="46" height="46"></object>
        </a>
        <ul class="nav col-md-4 justify-content-end">
          <li class="nav-item"><a href="https://github.com/Square-Pot/plant-lib" class="nav-link px-2 text-muted">GitHub</a></li>
          <li class="nav-item"><a href="https://www.youtube.com/@SuccsInTheNorth" class="nav-link px-2 text-muted">YouTube</a></li>
          <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">About</a></li>
        </ul>
      </footer>
    </div>

  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
