<script setup>
import QRCodeScanner from './QRCodeScanner.vue';
import PlantScanResult from './PlantScanResult.vue';
</script>

<script>
  import axios from 'axios'
  export default {
    props: {
        scanning: Boolean,
        multipleMode: Boolean,
        stopScanning: Boolean, 
    },
    data() {
      return {
          plant: '',
          show_scanner: false,
          show_intro: true,
          show_result: false,
          results: [],
          uids: [],
      }
    },
    watch: {
        scanning(){
            this.scanInit()
        },
        // stop(){
        //     this.scanStop()
        // },

    },
    methods: {
      onScan (decodedText, decodedResult) {
        // console.log(decodedText);
        // console.log(decodedResult);
        this.getData(decodedText);
      },
      async getData(uid) {
        try {
            const response = await axios.get('https://galangal.ru:8000/api/plant/' + uid);
            this.plant = response.data; 
            if (!this.multipleMode){
              this.stopScanning = !this.stopScanning;
              this.show_scanner = false;
              this.show_result = true;
              this.addNewResult(this.plant);
            } else {
              // add result 
              this.show_result = true;
              this.addNewResult(this.plant);
            }
        } catch (error) {
            console.log(error);
        }
      },
      scanInit(){
        if (this.show_scanner){
          this.show_intro = true;
          this.show_scanner = false;
          this.show_result = false;
        } else {
          this.show_intro = false;
          this.show_scanner = true;
          this.show_result = true;
        }
      },
      addNewResult(result_plant){
        if ( !result_plant.uid.includes(result_plant.uid) ){
          this.results.push(result_plant)
          this.uids.push(result_plant.uid)
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
      <p>Results: {{ results }}</p>
      <p>UIDs: {{ uids }}</p>
      <div class="px-4 my-4 text-center" v-if="show_scanner" >
        <div class="row justify-content-center my-3">
          <div class="col-10 d-flex justify-content-center">
            <QRCodeScanner :qrbox="250" :fps="10" style="width: 400px;" @result="onScan" :stop="stopScanning" />
            <div id="qr-code-full-region"></div>
          </div>
        </div>
      </div>

      <!-- Result -->
      <!-- <div class="px-4 pt-3 justify-content-center" v-if="show_result" > -->
      <div class="px-4 pt-3  my-4 text-center" v-if="show_result" >
        <div class="row justify-content-center my-3">
          <div class="col-10 d-flex justify-content-center">
              <ul>
                <PlantScanResult v-for="(plant, index) in results" :plant="plant" />
              </ul>  
          </div>
        </div>
      </div>
</template>