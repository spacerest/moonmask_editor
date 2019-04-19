import Route from '@ember/routing/route';
import { inject as service  } from '@ember/service';

export default Route.extend({
    store: service(),

    model(collage) {
        return this.get('store').peekRecord('collage', collage.collage_id);
    }

});
