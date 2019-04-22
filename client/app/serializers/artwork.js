import ApplicationSerializer from './application';
import DS from 'ember-data';


export default DS.JSONAPISerializer.extend({
  //keyForAttribute(key, method) {
  //  return dasherize(key);
  //}
//workaround to deal with apparent caching of previously underscored model attr
//names
    //attrs: {
    //    moonDate: 'moonDate',
    //    moonRelativeDate: 'moonRelativeDate',
    //    mainImageUrl: 'mainImageUrl',
    //    mainImageInstagramUrl: 'mainImageInstagramUrl',
    //    mainImageColor: 'mainImageColor',
    //    maskPositiveSpaceUrl: 'maskPositiveSpaceUrl',
    //    maskPositiveSpaceInstagramUrl: 'maskPositiveSpaceInstagramUrl',
    //    maskPositiveSpaceColor: 'maskPositiveSpaceColor',
    //    maskNegativeSpaceUrl: 'maskNegativeSpaceUrl',
    //    maskNegativeSpaceInstagramUrl: 'maskNegativeSpaceInstagramUrl',
    //    maskNegativeSpaceColor: 'maskNegativeSpaceColor',
    //    negativeSpaceTransparency: 'negativeSpaceTransparency',
    //    positiveSpaceTransparency: 'positiveSpaceTransparency',
    //    dimensionality: 'dimensionality'
    //}
});
