import Controller from '@ember/controller';
import { computed  } from '@ember/object';

export default Controller.extend({
    form: computed(function() {
        return {
            title: '',
            author: '',
            image: '',
            moonRelativeDate: '',
            moonDate: '',
            mainImageUrl: '',
            mainImageInstagramUrl:'',
            mainImageColor: '',
            maskPositiveSpaceUrl: '',
            maskPositiveSpaceInstagramUrl: '',
            maskPositiveSpaceColor: '',
            maskNegativeSpaceUrl: '',
            maskNegativeSpaceInstagramUrl:'',
            maskNegativeSpaceColor:'',
            negativeSpaceTransparency:'',
            positiveSpaceTransparency:'',
            dimensionality:'',
        }
    })
});
