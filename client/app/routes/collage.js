import Route from '@ember/routing/route';
import { inject as service  } from '@ember/service';

export default Route.extend({
    store: service(),

    model(collage) {
        return this.get('store').peekRecord('collage', collage.collage_id);
    },

    setupController(controller, model) {
        this._super(controller, model);
        this.controller.set('confirmingDelete', false);
        this.controller.set('isEditing', false);
        this.controller.set('form.description', model.get('description'));
    },

    actions: {
        delete(collage) {
            collage.deleteRecord();
            collage.save().then(() => {
                this.transitionTo('collages');
            });
        },

        update(collage) {
            const form = this.controller.get('form');

            collage.set('description', form.description);

            collage.save().then(() => {
                this.controller.set('isEditing', false);
            });
        }
    }

});
