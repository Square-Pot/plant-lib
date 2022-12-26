<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import Plants from './components/Plants.vue'
import QRCodeScanner from './components/QRCodeScanner.vue'
</script>

<script>
  export default {
    methods: {
      onScan (decodedText, decodedResult) {
        console.log(decodedText);
        console.log(decodedResult);

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
    <Plants />
    
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
