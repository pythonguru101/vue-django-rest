<template>
  <div class="container py-5">
    <h1 class="mb-4">Users</h1>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">User Id</th>
          <th scope="col">User Name</th>
          <th scope="col">Nick Name</th>
          <th scope="col">Phone</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, idx) in data" :key="idx">
          <th scope="row">{{idx + 1}}</th>
          <td>{{item.username}}</td>
          <td>{{item.first_name + ' ' + item.last_name}}</td>
          <td>{{item.nick_name}}</td>
          <td>{{item.phone}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapState } from 'vuex';
export default {
  name: 'about',
  computed: {
    ...mapState('users', ['data'])
  },
  mounted() {
    this.getAllUsers();
  },
  methods: {
    getAllUsers() {
      this.$store.dispatch("users/getAllUsers");
    },
  }
};
</script>
