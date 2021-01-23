<template>
  <div class="userlist">
    <h2>
      用户列表
    </h2>
    <ul>
      <li v-for="(item, index) in userlist" :key="'userlist' + index" @click="chooseuser(index)">
        <img :src="item.headerimg" />
        {{ item.username }}
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  data: function() {
    return {};
  },
  props: ["userlist"],
  methods:{
      chooseuser:function(index){
        //   console.log(index)
          this.$emit('chooseuser',index);
      }
  }
};
</script>
<style scoped>
ul > li > img {
  height: 50px;
  margin-left: 20px;
}

ul li {
  list-style: none;
}
.userlist {
  border: solid #585858;
}
</style>
