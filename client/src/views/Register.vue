<template>
  <div class="register-view">
    <template v-if="!registrationCompleted">
      <b-card
        title="Create Account"
      >
      <b-form @submit="onSubmit" @reset="onReset" class="register-form">
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
            placeholder="Enter user name"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="Your password:" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="form.password1"
            type="password"
            required
            placeholder="Enter password"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-3" label="Confirm password:" label-for="input-3">
          <b-form-input
            id="input-3"
            v-model="form.password2"
            type="password"
            required
            placeholder="Enter confirm password"
          ></b-form-input>
        </b-form-group>
        <b-form-group
          id="input-group-1"
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
          <b-button class="mr-3" type="submit" variant="primary" :disabled="registrationLoading">
            <b-spinner label="Spinning" variable="success" v-if="registrationLoading" class="mr-3"></b-spinner>
            Create Account
          </b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </div>
        <b-badge href="#" variant="danger" v-show="registrationError">
          An error occured while processing your request.
        </b-badge>
      </b-form>
      </b-card>
      <div class="mt-4">
        Already have an account?
        <router-link to="/login">Login</router-link>|
        <router-link to="/password_reset">Reset Password</router-link>
      </div>
    </template>
    <template v-else>
      <div>
        Registration complete. You should receive an email shortly with instructions on how to
        activate your account.
      </div>
      <div>
        <router-link to="/login">return to login page</router-link>
      </div>
    </template>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  data() {
    return {
      form: {
        username: '',
        password1: '',
        password2: '',
        email: '',
      },
    };
  },
  computed: mapState('signup', [
    'registrationCompleted',
    'registrationError',
    'registrationLoading',
  ]),
  methods: {
    ...mapActions('signup', [
      'createAccount',
      'clearRegistrationStatus',
    ]),
    onSubmit(evt) {
      evt.preventDefault();
      this.createAccount(this.form);
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.username = "";
      this.form.password1 = "";
      this.form.password2 = "";
      this.form.email = "";
    }
  },
  beforeRouteLeave(to, from, next) {
    this.clearRegistrationStatus();
    next();
  },
};
</script>

<style>
.register-view {
  min-height: 100vh;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.register-form {
  min-width: 350px;
}
</style>
