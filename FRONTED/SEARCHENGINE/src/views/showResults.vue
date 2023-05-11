<template>
  <div>



  </div>
</template>
<script>
export default {
data() {
  return {
    
  }
  },

  created() {
    const data = this.$router.currentRoute.params.id;
    console.log(data);
  },
}
</script>

<style lang="scss" scoped>

</style>