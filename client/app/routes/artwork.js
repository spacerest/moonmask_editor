import Route from '@ember/routing/route';
import { inject as service  } from '@ember/service';

export default Route.extend({
    store: service(),

    model(artwork) {
        return this.get('store').peekRecord('artwork', artwork.artwork_id);
    }
});
