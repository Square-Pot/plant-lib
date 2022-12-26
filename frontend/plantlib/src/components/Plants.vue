<script>
    import axios from 'axios'
    export default {
        data() {
            return {
                // plants
                plants: [''],
            }
        },
        methods: {
            async getData() {
                try {
                    // fetch plants
                    const response = await axios.get('http://localhost:8000/api/plant/' + this.uid);
                    // set the data returned as plants
                    this.plants = response.data; 
                } catch (error) {
                    // log the error
                    console.log(error);
                }
            },
        },
        created() {
            // Fetch plants on page load
            this.uid = '1|2';
            this.getData();
        }
    }
</script>

<template>
    <div class="plants_container">
        <div class="plants_content">
            <h1>Detected plant:</h1>
            <h2 v-bind="plants">{{ plants.genus }} {{ plants.species }}</h2>

            <!-- <ul class="plants_list">
                <li v-for="plant in plants" :key="plant.uid">
                    <h2>{{ plant.genus }} {{ plant.species }}</h2>
                    <p>{{ plant.description }}</p>
                    
                    <button @click="toggleTask(task)">
                        {{ plant.is_deleted ? 'Undo' : 'Complete' }}
                    </button>
                    <button @click="deletePlant(plant)">Delete</button>
                    
                </li>
            </ul> -->
            
        </div>
    </div>
</template>

<style>
</style>
