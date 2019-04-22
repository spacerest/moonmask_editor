import ApplicationSerializer from './application';
import DS from 'ember-data';


export default DS.JSONAPISerializer.extend({
    //serialize() {
    //    let payload = this._super(...arguments);
    //    delete payload.data.attributes.imageUrl;
    //    return payload;
    //}
    serializeAttribute: function(record, json, key, attribute) {
        if (attribute.name !== 'imageUrl' && attribute.name !== 'image_url') {
            this._super(record, json, key, attribute);
        }
    }
});
