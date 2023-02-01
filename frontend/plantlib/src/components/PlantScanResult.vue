<script>

export default {
    plant: {
        type: Object
    }
}

</script>

<template>
  <div class="card">
                <div class="card-body">
                  <h5 class="card-title fw-light">
                    <template v-if="plant.field_number"><span class="badge bg-secondary">{{ plant.field_number }}</span> </template>
                    <span class="fst-italic fw-normal">  {{ '  ' + plant.genus.charAt(0).toUpperCase() + plant.genus.slice(1) }}</span>
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
                  <p class="card-footer text-end"><small class="text-muted">UID: {{ plant.uid }}</small></p>
                </div>
              </div>
</template>