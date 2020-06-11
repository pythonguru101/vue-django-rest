<template>
  <div class="container py-5">
    <h1 class="mb-4">Shops</h1>
    <b-list-group>
      <b-list-group-item v-for="(item, idx) in data" :key="idx">
        <h2>{{item.name}}</h2>
        <div class="font-weight-bold font-italic">Created At: {{(new Date(item.created)).toLocaleString()}}</div>
        <p>{{item.content}}</p>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
import { mapState } from 'vuex';
export default {
  name: 'home',
  computed: {
    ...mapState('shops', ['data'])
  },
  mounted() {
    this.getAllShops();
  },
  methods: {
    getAllShops() {
      this.$store.dispatch("shops/getAllShops");
    },
  }
};
</script>

<style scoped>

</style>
