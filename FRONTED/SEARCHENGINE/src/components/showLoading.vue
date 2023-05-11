<template>
    <div>
    <div class="containerLoader"></div>
    <div class="query">
    <span>Preparing Result for: "{{ myquery }}"</span>
    </div>
    <br>
    <div>
    <div class="loader"></div>
    </div>


    </div>
</template>

<script>
export default {
    props: {
        myquery: {
            type:String
        }
    }
   
}
</script>

<style lang="css" scoped>
.loader {
  border: 8px solid #f3f3f3;
  border-top: 8px solid #3498db;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  animation: spin 2s linear infinite;
  margin: 50px auto;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
.containerLoader .query span
{
    font-weight: bold;
    color: white;


}

</style>