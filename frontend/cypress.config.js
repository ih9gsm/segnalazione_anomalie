const { defineConfig } = require('cypress');
const path = require('path');

module.exports = defineConfig({
  e2e: {
    supportFile: false,
    baseUrl: 'file://' + path.resolve(__dirname, 'src') + '/',
  },
});
