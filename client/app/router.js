import EmberRouter from '@ember/routing/router';
import config from './config/environment';

const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('collages');
  this.route('collage', { path: 'collages/:collage_id' });
  this.route('create-collage');
});

export default Router;
