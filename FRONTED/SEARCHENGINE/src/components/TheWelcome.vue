<script setup>

</script>
<template>
  <div>
  <div class="searchBar"> 
  <div class="logo">
   Custom Search engine
   {{ this.id }}
   </div> 
 <div class="items-wrapper">
  <input type="text" placeholder="search" v-model="query">
  <span class="search" @click="Search"><i class="fas fa-search" style="font-size: 3rem;"></i></span>
 </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      query:null
    }
  },
methods: {
    Search()
  {
    if(this.query!=null)
    {
      const searchUrl = `?q=${encodeURIComponent(this.query)}`;
      this.$router.push({ name: 'result', params: { string: searchUrl, id: this.query } });
    // window.location.replace(searchUrl);
    }

  }
},


  
}
</script>

<style lang="css" scoped>
.logo
{
  font-family: 'Gravitas One', cursive;
  font-size: xx-large;
  margin-bottom: 1rem;
  text-shadow: 0px 0px 1px red;
  text-align: center;

}
.searchBar
{
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.searchBar input
{
  padding: 10px;
  width: 80%;
  background: none;
  border: none;
  outline: none;
  color: white;
  font-weight: bold;
  
}

.items-wrapper
{
  width: 30rem;
  border-radius: 1.8rem;
  display: flex;
  justify-content: space-around;
  align-items: center;
  box-shadow: 0px 0px 1px white;
  padding: 5px;
  
}
@media (max-width: 500px)
{
 .items-wrapper
 {
   width:90%;
 }
 .logo
 {
  font-size: medium;
 }
}
.search
{
  cursor: pointer;
}
.search:active
{
  transform: scale(.9);

}



</style>