import Route from '@ember/routing/route';
import { inject as service  } from '@ember/service';

export default Route.extend({
    store: service(),

    model(artwork) {
        return this.get('store').peekRecord('artwork', artwork.artwork_id);
    },

    setupController(controller, model) {
        this._super(controller, model);
        this.controller.set('confirmingDelete', false);
        this.controller.set('isEditing', false);
    },

    actions: {
        delete(artwork) {
            artwork.deleteRecord();
            artwork.save().then(() => {
                this.transitionTo('artworks');
            });
        },

        update(artwork) {
            const form = this.controller.get('form');

            artwork.set('title', form.title);
            artwork.set('moonRelativeDate', form.moonRelativeDate);
            artwork.set('moonDate', form.moonDate);
            artwork.set('mainImageUrl', form.mainImageUrl);
            artwork.set('mainImageInstagramUrl', form.mainImageInstagramUrl);
            artwork.set('mainImageColor', form.mainImageColor);
            artwork.set('maskPositiveSpaceUrl', form.maskPositiveSpaceUrl);
            artwork.set('maskPositiveSpaceInstagramUrl', form.maskPositiveSpaceInstagramUrl);
            artwork.set('maskPositiveSpaceColor', form.maskPositiveSpaceColor);
            artwork.set('maskNegativeSpaceUrl', form.maskNegativeSpaceUrl);
            artwork.set('maskNegativeSpaceInstagramUrl', form.maskNegativeSpaceInstagramUrl);
            artwork.set('maskNegativeSpaceColor', form.maskNegativeSpaceColor);
            artwork.set('negativeSpaceTransparency', form.negativeSpaceTransparency);
            artwork.set('positiveSpaceTransparency', form.positiveSpaceTransparency);
            artwork.set('dimensionality', form.dimensionality);

            artwork.save().then(() => {
                this.controller.set('isEditing', false);
            });
        }
    }
});
