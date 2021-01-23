<template>
  <div>
    <el-row :gutter="8">
      <el-col :span="18">
        <el-input type="text" v-model="value"></el-input>
      </el-col>
      <el-col :span="5">
        <el-button>
            发送
        </el-button>
      </el-col>
    </el-row>
  </div>
</template>
<script>
export default {
  data: function() {
    return {
      value: "",
    };
  },
};
</script>

<style scoped></style>
