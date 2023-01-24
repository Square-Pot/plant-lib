<script setup>
import IconMainLogo from './components/icons/IconMainLogo.vue'
import IconMiniLogo from './components/icons/IconMiniLogo.vue'
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

<style>
    html {min-width: 375px}
  </style>

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
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <a class="navbar-brand" href="#"><IconMainLogo /></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Link</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropdown
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
              </ul>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
            </li>
          </ul>
          <form class="d-flex">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>


    <!-- Scaner -->
    <div class="container text-center" style="min-height: 500px;">

      <Scan :scanning="scanningOn" />

    </div>

    <!-- Buttons desktop -->
    <div class="container py-4 text-center" >
      <div class="d-none d-sm-none d-md-none d-lg-block d-xl-block d-xxl ">
        <div class="md-flex justify-content-between bg-light bg-gradient py-2">
          <button class="btn btn-lg px-4 mx-2 btn-success" type="button" @click="scanToggle">Scan</button>
          <button class="btn btn-lg px-4 mx-2 btn-outline-dark" type="button">Plants</button>
          <button class="btn btn-lg px-4 mx-2 btn-outline-dark" type="button">Labels</button>
        </div>
      </div>
    </div>

    <!-- Buttons Mobile -->
    <div class="container py-4 text-center" >
      <div class="fixed-bottom  d-block d-sm-block d-md-block d-lg-none ">
        <div class="md-flex justify-content-between bg-light bg-gradient py-2 shadow-lg">
          <button class="btn btn-lg px-4 mx-2 btn-success" type="button" @click="scanToggle">Scan</button>
          <button class="btn btn-lg px-4 mx-2 btn-outline-dark" type="button">Plants</button>
          <button class="btn btn-lg px-4 mx-2 btn-outline-dark" type="button">Labels</button>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="container d-none d-lg-block ">
      <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
        <p class="col-md-4 mb-0 text-muted">© 2023 Dmitry Natkha</p>
        <a href="/" class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
          <IconMiniLogo />
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
