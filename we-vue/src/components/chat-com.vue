<template>
  <div class="chat">
    <h1>{{ currentuser.username }}</h1>
    <chatin-formatiom></chatin-formatiom>
    <!-- <chat-input></chat-input> -->
    <chat-text>
    </chat-text>
   <chat-input></chat-input>
  </div>
</template>

<script>
import chatinFormatiom from "./chat-information"
import chatInput from "./chat-input"
import chatText from './chat-text'

export default {
  props: ["currentuser"],
  components: {
    chatinFormatiom,chatInput,chatText
  },
};
</script>

<style scope>
.chat {
  width: 500px;
  height: 500px;
  border: rgb(144, 144, 144) solid;
}
</style>
