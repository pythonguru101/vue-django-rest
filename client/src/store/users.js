import users from '../api/users';
import { LOADING_START, SET_DATA, LOADING_SUCCESS, LOADING_FAILURE } from './types';

const initialState = {
  loading: false,
  error: false,
  data: null,
};

const getters = {
  data: state => state.data,
};

const actions = {
  getAllUsers({ commit }) {
    commit(LOADING_START);
    return users.allUsers()
      .then(({ data }) => commit(SET_DATA, data))
      .then(() => commit(LOADING_SUCCESS))
      .catch(() => commit(LOADING_FAILURE));
  },
};

const mutations = {
  [LOADING_START](state) {
    state.loading = true;
    state.error = false;
  },
  [LOADING_FAILURE](state) {
    state.loading = false;
    state.error = true;
  },
  [LOADING_SUCCESS](state) {
    state.loading = false;
    state.error = false;
  },
  [SET_DATA](state, data) {
    state.data = data;
  },
};

export default {
  namespaced: true,
  state: initialState,
  getters,
  actions,
  mutations,
};
