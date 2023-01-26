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
            const response = await axios.get('https://galangal.ru:8000/api/plant/' + uid);
            this.plant = response.data; 
            this.scanning = false;
            this.show_scanner = false;
            this.show_result = true;
        } catch (error) {
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
      <div class="px-4 my-4 text-center" v-if="show_scanner" >
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

              <div class="card" style="width: 18rem;">
                <div class="card-body">
                  <h5 class="card-title fw-light">
                    <template v-if="plant.field_number"><span class="fs-6">{{ plant.field_number }}    </span></template>
                    <span class="fst-italic fw-normal">{{ plant.genus.charAt(0).toUpperCase() + plant.genus.slice(1) }}</span>
                    <template v-if="plant.species">  sp. <span class="fst-italic fw-normal">{{ plant.species }}</span></template>
                    <template v-if="plant.subspecies">  ssp. <span class="fst-italic fw-normal">{{ plant.subspecies }}</span></template>
                    <template v-if="plant.variety">  var. <span class="fst-italic fw-normal">{{ plant.variety }}</span></template>
                    <template v-if="plant.cultivar">  cv. '<span class="fst-italic fw-normal">{{ plant.cultivar }}</span>'</template>
                  </h5>
                  <table class="table" style="font-size:0.80em;">
                    <tbody>
                      <tr>
                        <th scope="row">Age:</th>
                        <td>{{ plant.date_purchase }}</td>
                      </tr>
                      <tr  v-if="plant.source">
                        <th scope="row">Source:</th>
                        <td>{{ plant.source }}</td>
                      </tr>
                      <tr v-if="plant.form">
                        <th scope="row">Form:</th>
                        <td>{{ plant.form }}</td>
                      </tr>
                      <tr v-if="plant.affinity">
                        <th scope="row">Affinity:</th>
                        <td>{{ plant.affinity }}</td>
                      </tr>
                      <tr v-if="plant.ex">
                        <th scope="row">Ex:</th>
                        <td>{{ plant.ex }}</td>
                      </tr>
                      <tr v-if="plant.geography">
                        <th scope="row">Geography:</th>
                        <td>{{ plant.geography }}</td>
                      </tr>
                      <tr v-if="plant.price">
                        <th scope="row">Price:</th>
                        <td>{{ plant.price }}</td>
                      </tr>
                      <tr v-if="plant.user_number">
                        <th scope="row">Custom number:</th>
                        <td>{{ plant.user_number }}</td>
                      </tr>
                    </tbody>
                  </table>
                  <p class="card-text" v-if="plant.info">{{ plant.info }}</p>
                  <p class="card-text" v-if="plant.description">{{ plant.description }}</p>
                  <p class="card-text"><small class="text-muted">UID: {{ plant.uid }}</small></p>
                </div>
              </div>
                
          </div>
        </div>
      </div>
</template>