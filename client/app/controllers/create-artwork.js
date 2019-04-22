import Controller from '@ember/controller';
import { computed  } from '@ember/object';

export default Controller.extend({
    form: computed(function() {
        return {
            title: '',
            image: '',
            moon_relative_date: '',
            moon_date: '',
            main_image_url: '',
            main_image_instagram_url:'',
            main_image_color: '',
            mask_positive_space_url: '',
            mask_positive_space_instagram_url: '',
            mask_positive_space_color: '',
            mask_negative_space_url: '',
            mask_negative_space_instagram_url:'',
            mask_negative_space_color:'',
            negative_space_transparency:'',
            positive_space_transparency:'',
            dimensionality:'',

            //title: '',
            //image: '',
            //moon_relative_date: '',
            //moon_date: '',
            //main_image_url: '',
            //main_image_instagram_url:'',
            //main_image_color: '',
            //mask_positive_space_url: '',
            //mask_positive_space_instagram_url: '',
            //mask_positive_space_color: '',
            //mask_negative_space_url: '',
            //mask_negative_space_instagram_url:'',
            //mask_negative_space_color:'',
            //negative_space_transparency:'',
            //positive_space_transparency:'',
            //dimensionality:'',
        }
    })
});
