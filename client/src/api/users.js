import session from './session';

export default {
  allUsers() {
    return session.get('/api/users/');
  },
};
