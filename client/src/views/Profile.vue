<template>
  <div class="container py-5">
    <h1 class="mb-4">Profile</h1>
    <b-card>
      <b-form class="register-form">
        <b-form-group
          id="input-group-1"
          label="User name:"
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            v-model="form.username"
            type="text"
            required
            readonly
            placeholder="Enter user name"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="Your password:" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="form.first_name"
            required
            placeholder="Enter password"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-3" label="Confirm password:" label-for="input-3">
          <b-form-input
            id="input-3"
            v-model="form.last_name"
            required
            placeholder="Enter confirm password"
          ></b-form-input>
        </b-form-group>
        <b-form-group
          id="input-group-4"
          label="Email address:"
          label-for="input-4"
        >
          <b-form-input
            id="input-4"
            v-model="form.email"
            type="email"
            required
            placeholder="Enter user email"
          ></b-form-input>
        </b-form-group>
        <div class="d-flex justify-content-center">
          <b-button class="mr-3" type="submit" variant="primary" >
            <!-- <b-spinner label="Spinning" variable="success" v-if="registrationLoading" class="mr-3"></b-spinner> -->
            Update
          </b-button>
        </div>
      </b-form>
      </b-card>
  </div>
</template>

<script>
import { mapState } from 'vuex';
export default {
  name: 'about',
  data() {
    return {
      form: {
        username: '',
        first_name: '',
        last_name: '',
        email: '',
      },
    };
  },
  computed: {
    ...mapState('auth', ['userData'])
  },
  mounted() {
    this.getUserInfo();
  },
  methods: {
    getUserInfo() {
      this.$store.dispatch("auth/getAccountDetails")
        .then(()=>{          
          this.form.username = this.userData.username;
          this.form.first_name = this.userData.first_name;
          this.form.last_name = this.userData.last_name;
          this.form.email = this.userData.email;
          
        });
    },
  }
};
</script>
