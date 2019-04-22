import Route from '@ember/routing/route';
import { inject as service  } from '@ember/service';

export default Route.extend({
    store: service(),

    setupController(controller, model) {
        this._super(controller, model);

        this.controller.set('form.title', '');
        this.controller.set('form.moon_relative_date', '');
        this.controller.set('form.moon_date', '');
        this.controller.set('form.main_image_url', '');
        this.controller.set('form.main_image_instagram_url', '');
        this.controller.set('form.main_image_color', '');
        this.controller.set('form.mask_positive_space_url', '');
        this.controller.set('form.mask_positive_space_instagram_url', '');
        this.controller.set('form.mask_positive_space_color', '');
        this.controller.set('form.mask_negative_space_url', '');
        this.controller.set('form.mask_negative_space_instagram_url', '');
        this.controller.set('form.mask_negative_space_color', '');
        this.controller.set('form.negative_space_transparency', '');
        this.controller.set('form.positive_space_transparency', '');
        this.controller.set('form.dimensionality', '');
    },

    actions: {
        create() {
            const form = this.controller.get('form');
            const store = this.get('store');

            const newArtwork = store.createRecord('artwork', {
                title: form.title,
                moonRelativeDate: form.moonRelativeDate,
                moonDate: form.moonDate,
                mainImageUrl: form.mainImageUrl,
                mainImageInstagramUrl: form.mainImageInstagramUrl,
                mainImageColor: form.mainImageColor,
                maskPositiveSpaceUrl: form.maskPositiveSpaceUrl,
                maskPositiveSpaceInstagramUrl: form.maskPositiveSpaceInstagramUrl,
                maskPositiveSpaceColor: form.maskPositiveSpaceColor,
                maskNegativeSpaceUrl: form.maskNegativeSpaceUrl,
                maskNegativeSpaceInstagramUrl: form.maskNegativeSpaceInstagramUrl,
                maskNegativeSpaceColor: form.maskNegativeSpaceColor,
                negativeSpaceTransparency: form.negativeSpaceTransparency,
                positiveSpaceTransparency: form.positiveSpaceTransparency,
                dimensionality: form.dimensionality,
            });

            newArtwork.save()
                .then(() => {
                    this.transitionTo('artworks');
                });
        },

        cancel() {
            this.transitionTo('artworks');
        }

    }
});
