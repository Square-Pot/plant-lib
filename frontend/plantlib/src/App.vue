<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import Plants from './components/Plants.vue'
import QRCodeScanner from './components/QRCodeScanner.vue'
</script>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
          plant: '',
          show_scanner: false,
          show_intro: true,
          show_result: false,
      }
    },
    methods: {
      onScan (decodedText, decodedResult) {
        // console.log(decodedText);
        // console.log(decodedResult);
        this.getData(decodedText);

      },
      async getData(uid) {
        try {
            // fetch plants
            const response = await axios.get('http://localhost:8000/api/plant/' + uid);
            // set the data returned as plants
            this.plant = response.data; 
            this.show_scanner = false;
            this.show_result = true;
        } catch (error) {
            // log the error
            console.log(error);
        }
      },
      scanInit (){
        if (this.show_scanner){
          this.show_intro = true;
          this.show_scanner = false;
          this.show_result = false;
        } else {
          this.show_intro = false;
          this.show_scanner = true;
          this.show_result = false;
        }
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

      <!--Intro -->
      <div class="px-4 pt-3  my-4 text-center" v-if="show_intro">
        <h1 class="display-4 fw-bold">Organize your plants</h1>
        <div class="col-lg-6 mx-auto">
          <p class="lead mb-4">Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.</p>
        </div>
        <div class="container px-5">
          <img src="/src/assets/main_page.jpg" class="img-fluid border rounded-3 shadow-lg mb-2" alt="Plant Lib" width="700" height="500" loading="lazy">
        </div>
      </div>

      <!-- Scanner -->
      <div class="px-4 pt-3  my-4 text-center" v-if="show_scanner" >
        <div class="row justify-content-center my-3">
          <div class="col-10 d-flex justify-content-center">
            <QRCodeScanner :qrbox="250" :fps="10" style="width: 400px;" @result="onScan" />
            <div id="qr-code-full-region"></div>
          </div>
        </div>
      </div>

      <!-- Result -->
      <!-- <div class="px-4 pt-3 justify-content-center" v-if="show_result" > -->
      <div class="px-4 pt-3  my-4 text-center" v-if="show_result" >
        <div class="row justify-content-center my-3">
          <div class="col-10 d-flex justify-content-center">
            <div class="card justify-content-center  mb-3" style="max-width: 540px;" >
              <div class="row g-0">
                <div class="col-md-4">
                  <img src="/src/assets/plant_example.jpg" class="img-fluid rounded-start" alt="{{ plant.genus }}">
                </div>
                <div class="col-md-8">
                  <div class="card-body">
                    <h5 class="card-title">{{ plant.genus }}</h5>
                    <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                    <p class="card-text"><small class="text-muted">UID: {{ plant.uid }}</small></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>

    <!-- Buttons -->
    <div class="container py-4 text-center" >
      <div class="d-grid gap-2 d-md-flex justify-content-md-center">
        <button class="btn btn-lg px-4 btn-success" type="button" @click="scanInit">Scan</button>
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
