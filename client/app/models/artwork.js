import DS from 'ember-data';

export default DS.Model.extend({
    title: DS.attr(),
    imageUrl: DS.attr(),
    moonDate: DS.attr(),
    moonRelativeDate: DS.attr(),
    mainImageUrl: DS.attr(),
    mainImageInstagramUrl: DS.attr(),
    mainImageColor: DS.attr(),
    maskPositiveSpaceUrl: DS.attr(),
    maskPositiveSpaceInstagramUrl: DS.attr(),
    maskPositiveSpaceColor: DS.attr(),
    maskNegativeSpaceUrl: DS.attr(),
    maskNegativeSpaceInstagramUrl: DS.attr(),
    maskNegativeSpaceColor: DS.attr(),
    negativeSpaceTransparency: DS.attr(),
    positiveSpaceTransparency: DS.attr(),
    dimensionality: DS.attr(),
});
