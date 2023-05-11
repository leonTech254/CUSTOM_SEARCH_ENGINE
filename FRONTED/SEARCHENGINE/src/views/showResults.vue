<template>
  <div>



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