// src/setupProxy.js
const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function (app) {
  app.use(
    createProxyMiddleware() {
      target: 'https://rpgplant.kro.kr',
      changeOrigin: true,
      pathRewrite: {
        '^/': '',
      }
    }),
  );
};