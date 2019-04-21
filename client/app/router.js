import EmberRouter from '@ember/routing/router';
import config from './config/environment';

const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('artworks');
  this.route('artwork', { path: 'artworks/:artwork_id' });
  this.route('create-artwork');
});

export default Router;
