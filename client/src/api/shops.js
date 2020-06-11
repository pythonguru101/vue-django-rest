import session from './session';

export default {
  allShops() {
    return session.get('/api/shops/');
  },
};
