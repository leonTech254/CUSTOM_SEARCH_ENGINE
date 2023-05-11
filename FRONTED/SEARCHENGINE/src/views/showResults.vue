<script setup>
import showLoading from '../components/showLoading.vue'

</script>

<template>
  <div class="containerWrapper">

          <showLoading id="showLoading" :myquery="search" />

          <div class="topsearchbar">
              <div class="searchBar">
                  <div class="logo">
                      Custom Search <br> engine
                  </div>
                  <div>
                      <div class="items-wrapper">
                          <input type="text" placeholder="search" v-model="query">
                          <span class="search" @click="Searchquery"><i class="fas fa-search"
                                  style="font-size: 1rem;"></i></span>
                      </div>
                  </div>
              </div>

          </div>
          <div class="seperator"></div>
          <div class="cartegorybar">
              <div class="tabs">
                  <span>showing result for "{{ search }}"</span>
              </div>
              <div class="showResults">
                  <ul>
                      <li v-for="(result, index) in results" :key="index" class="resultBlock">
                          <div class="link">
                              <a :href="result.url">{{ result.url }}</a>
                          </div>
                          <div class="title">{{ result.title }} </div>
                          <div class="content">{{ result.snippet }}</div>
                      </li>
                  </ul>

              </div>
          </div>
      </div>
</template>
<script>
export default {
data() {
    return {
    search:null
    
  }
  },

  created() {
    const data = this.$route.params.id;
    this.search=data
    console.log(data);
  },
}
</script>

<style lang="scss" scoped>

</style>