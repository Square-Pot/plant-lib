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
          scan_button_name: 'Scan'
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
            console.log(this.plant);
        } catch (error) {
            // log the error
            console.log(error);
        }
      },
      toggleScannerShowing (){
        this.show_scanner = !this.show_scanner;
        if (this.show_scanner){
          this.scan_button_name = 'Hide scanner';
        } else {
          this.scan_button_name = 'Scan again!';
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

    <div class="container">
      <div class="col-md-3">
          <button type="button" class="btn btn-outline-dark me-2" @click="toggleScannerShowing">{{ scan_button_name }}</button>
      </div>
    </div>

    <div v-if="show_scanner" class="container">
      <QRCodeScanner :qrbox="250" :fps="10" style="width: 500px;" @result="onScan" />
      <div id="qr-code-full-region"></div>
      <h2 v-if="plant.uid"><b>{{ plant.uid }}</b> - {{ plant.genus }} {{ plant.species }}</h2>
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
