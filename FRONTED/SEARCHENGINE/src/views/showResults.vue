<script setup>
import showLoading from '../components/showLoading.vue';
import ToEternalLink from '../components/ToExternalLink.vue';

</script>

<template>
  <div>
  <div class="resultPage">
  <div class="hideResult" v-if="show">
  <showLoading :myquery="query" />
  </div>

  <div class="hideResult" v-if="showEternal">
    <ToEternalLink :myquery="query"/>
  </div>
  <div class="topWrapper">
  <div class="topbar">
    <div class="logo">
    <span>
    Custom search engine
    </span>
    </div>
   <div class="inputContainer">
    <input type="text" v-model="querySearch">
    <span class="search" @click="Searchquery"><i class="fas fa-search" style="font-size: 1.5rem;"></i></span>
   </div>
    </div>
  </div>
  <div class="emptydiv">
      
      </div>
  <div class="searchResultsContainer">
  <div class=""></div>
  <div class="resutsWrapper">
  <div class="indicateResult">showing result for <span>{{ query }}</span></div>
  <ul>
  <li v-for="(result, index) in results" :key="index" class="resultBlock">
    <div class="link">
    <span class="customLink" @click="checkResults(result.url)" >{{ result.url }}</span>
      <!-- <a :href="result.url">{{ result.url }}</a> -->
    </div>
    <div class="title">{{ result.title }} </div>
    <div class="content">{{ result.snippet }}</div>
  </li>
        </ul>
  </div>
  
  </div>  
  </div>

  </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
      return {
        query: null,
        show: true,
        results: [],
        showEternal: false,
        querySearch:true
      }
  },
  methods: {
      Searchquery() {
      if (this.query != null) {
        this.show = true
        const searchUrl = `?q=${encodeURIComponent(this.query)}`;
        this.$router.push({ name: 'result', params: { string: searchUrl, id: this.query } });
         const data = this.querySearch;
        this.query = this.querySearch
        axios.post("/search", { "query": data })
          .then((res) => {
            this.results = res.data.result
            this.show = false;
          })
          .catch((err) => {

          })

        

      }
    },
    checkResults(value)
    {
      this.show = true
      this.showEternal = true;
      this.query = value;
      setTimeout(() => {
        location.href = value;
      },5000)

    }
      
  },
  created() {
    const data = this.$route.params.id;
    this.query = data
    this.querySearch=data
    axios.post("/search", { "query": data })
      .then((res) => {
        this.results = res.data.result
        this.show = false;
      })
      .catch((err) => {

      })

  },
    
  }
</script>

<style lang="css" scoped>
*
{
  list-style: none;
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

.hideResult
{
  min-height: 100vh;
  position: fixed;
  background-color: var(--color-background);
  z-index: 30;
  width: 100%;
  text-align: center;

  display: flex;
  flex-direction: column;
  justify-content: center;
}

.emptydiv
{
  /* margin: 1rem; */
  padding-bottom:100px ;
}
.topbar
{
  display: grid;
  grid-template-columns: repeat(5,1fr);
  text-align: center;
  gap: 2rem;
  background-color: var(--color-background);
  /* margin-top: -1rem; */
}

.topWrapper
{
  width: 100%;
  position: fixed;
  padding: 15px;
  z-index: 10;
}
.logo  span{
  font-family: 'Gravitas One', cursive;
  font-size: medium;
  margin-bottom: 1rem;
  text-align: center;
}

.inputContainer
{
  border: 1px solid white;
  border-radius: 3rem;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.indicateResult span
{
  color: green;
  font-weight: bolder;
}
.indicateResult,ul
{
  padding-left: 10px;
}

.resutsWrapper
{
  padding-top: 10px;
}
@media (min-width:500px)
{
  .inputContainer
  {
      grid-column: 2/4;
  }
  .resutsWrapper
  {
    grid-column: 2/5;
    padding-left: 5px;
  }
}

.inputContainer input {
  width: 80%;
  background: none;
  border: none;
  outline: none;
  color: white;
  font-weight: bold;
  padding: 10px;
}

.searchResultsContainer
{
  display: grid;
  grid-template-columns: repeat(5,1fr);
  gap: .5rem;
}

/* small devices */

@media (max-width:500px)
{
  .topbar
  {
    grid-template-columns: repeat(1,1fr);

  }
  .searchResultsContainer
{
  grid-template-columns: repeat(1,1fr);
}

}
.customLink
{
  color: cyan;
  text-decoration: underline;
}



</style>