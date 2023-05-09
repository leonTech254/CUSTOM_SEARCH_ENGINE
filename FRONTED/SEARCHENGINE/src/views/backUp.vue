<template>
  <div class="containerWrapper">
    <div class="topsearchbar">

      <div class="searchBar">

        <div class="logo">
          Custom Search <br> engine
        </div>
        <div>
          <div class="items-wrapper">
            <input type="text" placeholder="search" v-model="query">
            <span class="search" @click="Search"><i class="fas fa-search" style="font-size: 1rem;"></i></span>
          </div>


        </div>
      </div>
      <div class="cartegorybar">
        <div class="tabs">
          <span>all</span>
          <span>images</span>
        </div>
        <div class="showResults">
          <ul>
            <li v-for="(result, index) in results" :key="index">
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
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['string', 'id'],
  data() {
    return {
      results: []
    }
  },
  created() {
    axios.post("/search", { "query": this.$route.params.id })
      .then((res) => {
        this.results = res.data.result
        console.log(this.result)

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
  background-color: rebeccapurple;

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
  position: fixed;
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
}
</style>