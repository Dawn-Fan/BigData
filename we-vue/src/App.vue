<template>
  <div id="app">
    <div class="main">
      <chatCom :currentuser="currentuser"></chatCom>
      <userList
        :userlist="userlist"
        @chooseuser="changeuser"
      ></userList>
     
    </div>
  </div>
</template>

<script>
import chatCom from "./components/chat-com";
import userList from "./components/userlist-com";

export default {
  name: "App",
  components: {
    chatCom,
    userList,
  },
  data: function() {
    return {
      msg: "聊天软件",
      userlist: [
        {
          username: "小米",
          headerimg: require("./assets/img/vue1.jpg"),
        },
        {
          username: "小花",
          headerimg: require("./assets/img/vue2.jpg"),
        },
        {
          username: "小红",
          headerimg: require("./assets/img/vue3.jpg"),
        },
        {
          username: "小绿",
          headerimg: require("./assets/img/vue4.jpg"),
        },
      ],
      currentuser: {
        username: "小绿",
        headerimg: require("./assets/img/vue4.jpg"),
      },
    };
  },
  methods: {
    changeuser: function(index) {
      console.log(index
      );
      // console.log(this.userlist[index].username);
      this.currentuser = this.userlist[index];
    },
  },
};
</script>

<style scoped>
.main {
  display: flex;
}</style
>>
