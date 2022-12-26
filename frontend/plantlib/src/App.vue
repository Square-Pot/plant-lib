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
          plant: ''
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
      }
    }
  }
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <!--
    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
    -->

  </header>

  <main>
    <!-- TheWelcome /-->
    <QRCodeScanner 
      :qrbox="250" 
      :fps="10" 
      style="width: 500px;"
      @result="onScan"
    />
    <!-- <Plants /> -->
    <h2 v-bind="plant"><b>{{ plant.uid }}</b> - {{ plant.genus }} {{ plant.species }}</h2>
    
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
