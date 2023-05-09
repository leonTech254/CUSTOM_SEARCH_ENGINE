<script setup>
import showLoading from '../components/showLoading.vue'

</script>

<template>
  <div class="containerWrapper">
 
  <showLoading id="showLoading" v-if="show" :myquery="this.$route.params.id"/>
  
    <div class="topsearchbar">
      <div class="searchBar">
        <div class="logo">
          Custom Search <br> engine
        </div>
        <div>
          <div class="items-wrapper">
            <input type="text" placeholder="search" v-model="query">
            <span class="search" @click="Searchquery"><i class="fas fa-search" style="font-size: 1rem;"></i></span>
          </div>
        </div>
      </div>

      </div>
      <div class="seperator"></div>
      <div class="cartegorybar">
        <div class="tabs">
          <span>showing result for "{{ this.$route.params.id }}"</span>
        </div>
        <div class="showResults">
          <ul>
            <li v-for="(result, index) in results" :key="index"  class="resultBlock">
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
import axios from 'axios';

export default {
  props: ['string', 'id'],
  data() {
    return {
      results: [],
      query: null,
      show:true
    }
  },
  methods: {
    Searchquery()
    {
     
     
      if (this.query != null) {
         this.show= true
        const searchUrl = `?q=${encodeURIComponent(this.query)}`;
        this.$router.push({ name: 'result', params: { string: searchUrl, id: this.query } });
        this.search_two()
        // window.location.replace(searchUrl);
        
      }
    },
    search_two() {
      // location.reload();
      this.query = this.$route.params.id;
      axios.post("/search", { "query": this.$route.params.id })
        .then((res) => {
          this.results = res.data.result
          console.log(this.result)
          this.show = false;


        })
        .catch((err) => {

        })

    },
  },
 
  created() {
    this.query = this.$route.params.id;
    axios.post("/search", { "query": this.$route.params.id })
      .then((res) => {
        this.results = res.data.result
        console.log(this.result)
        this.show = false;
      })
      .catch((err) => {

      })
  },

}
</script>

<style lang="css" scoped>
.containerWrapper {
  width: 100vw;
  min-height: 100vh;

}


.seperator
{
  margin-top:.1rem;
  padding-bottom: 100px;
}

.logo {
  font-family: 'Gravitas One', cursive;
  font-size: medium;
  margin-bottom: 1rem;
  text-shadow: 0px 0px 1px red;
  text-align: center;
  width: 15rem;

}

.topsearchbar {
  padding: 10px;
  padding-top: 20px;
  padding-bottom: 20px;
  position: fixed;
  background-color:  var(--color-background);;
  z-index: 2;
  width: 100%;
}

.searchBar {
  width: 100%;
  display: flex;
  gap: 1.5rem;
}

.searchBar input {
  width: 80%;
  background: none;
  border: none;
  outline: none;
  color: white;
  font-weight: bold;
  padding: 10px;
}

.items-wrapper {
  width: 30rem;
  border-radius: 2.8rem;
  display: flex;
  justify-content: space-around;
  align-items: center;
  box-shadow: 0px 0px 1px white;

}

.search {
  cursor: pointer;
}

.search:active {
  transform: scale(.9);

}

.tabs {
  display: flex;
  align-items: center;
  gap: .5rem;
  width: 100%;
  padding-top: 10px;

}

.tabs span {
  cursor: pointer;
  font-size: medium;
  text-transform: capitalize;
}

.tabs span:hover {
  font-weight: bold;
  text-decoration: underline;
}

.cartegorybar {
  padding-left: 15rem;
  width: 80%;
}

.showResults ul li {
  list-style: none;
}

.showResults .title {
  text-transform: capitalize;
  font-weight: bold;
  font-size: large;
  color: white;
}
.resultBlock
{
  margin-bottom: .5rem;
  border-bottom: .2px solid white;
  padding: 10px;
}
#showLoading
{
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: fixed;
  background-color: var(--color-background);
  z-index: 10;
}


@media (max-width:500px)
{
  *
  {
    padding: 0;
    width: 0;
  
  }
  .logo
  {
    font-size: xx-small;
    width: 10%;
  }
  .cartegorybar
  {
    padding: 0;
    width: 90%;
  }
  .containerWrapper
{
  width: 90%;
}
.items-wrapper
{
  width: 100%;
}
.searchBar
{
  gap: 1rem;
  width: 100%;
  
}
.searchBar input
{
  width: 100%;
}
.cartegorybar
{
  width: 100%;
  text-align: justify;
}
}
</style>