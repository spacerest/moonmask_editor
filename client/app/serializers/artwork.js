import ApplicationSerializer from './application';
import DS from 'ember-data';


export default DS.JSONAPISerializer.extend({
    serializeAttribute: function(record, json, key, attribute) {
        if (attribute.name !== 'image') {
            this._super(record, json, key, attribute);
        }
    }
});
