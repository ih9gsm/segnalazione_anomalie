const { add } = require('../src/utils');

test('adds numbers', () => {
  expect(add(2, 3)).toBe(5);
});
