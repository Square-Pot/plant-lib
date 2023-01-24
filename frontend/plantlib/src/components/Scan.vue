<script setup>
import QRCodeScanner from './QRCodeScanner.vue'
</script>

<script>
  import axios from 'axios'
  export default {
    props: {
        scanning: Boolean,
    },
    data() {
      return {
          plant: '',
          show_scanner: false,
          show_intro: true,
          show_result: false,
      }
    },
    watch: {
        scanning(new_val, old_val){
            this.scanInit()
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

    <!--Intro -->
    <div class="px-4 my-3 text-center" v-if="show_intro">
        <h1 class="display-4 fw-bold">Organize your plants</h1>
        <div class="col-lg-6 mx-auto">
          <p class="lead mb-4">Organize the data about your plant collection and use an automatic tool to create labels with Data Matrices for quick identification of your plants.</p>
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

</template>