import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Route | create-artwork', function(hooks) {
  setupTest(hooks);

  test('it exists', function(assert) {
    let route = this.owner.lookup('route:create-artwork');
    assert.ok(route);
  });
});
