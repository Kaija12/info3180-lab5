<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

function fetchMovies() {
  fetch('/api/v1/movies')
    .then(response => response.json())
    .then(data => { movies.value = data.movies; });
}

onMounted(() => { fetchMovies(); });
</script>

<template>
  <div>
    <h2>Movies</h2>
    <div class="row">
      <div v-for="movie in movies" :key="movie.id" class="col-md-6 mb-3">
        <div class="card d-flex flex-row p-2">
          <img :src="movie.poster" alt="poster" style="width:100px; height:150px; object-fit:cover;" />
          <div class="ms-3">
            <h5>{{ movie.title }}</h5>
            <p>{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>