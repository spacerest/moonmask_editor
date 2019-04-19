import Route from '@ember/routing/route';
import { inject as service  } from '@ember/service';

export default Route.extend({
    store: service(),

    setupController(controller, model) {
        this._super(controller, model);
        this.controller.set('form.description', '');
    },

    actions: {
        create() {
            const form = this.controller.get('form');
            const store = this.get('store');

            const newCollage = store.createRecord('collage', {
                description: form.description,
            });

            newCollage.save()
                .then(() => {
                    this.transitionTo('collages');
                });
        },

        cancel() {
            this.transitionTo('collages');
        }
    }
});
