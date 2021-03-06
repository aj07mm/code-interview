var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')


module.exports = {
  context: __dirname,
  entry: [
      'webpack-dev-server/client?http://localhost:3000',
      'webpack/hot/only-dev-server',
      './assets/js/apps/home/index.jsx',
      './assets/js/apps/book_list/index.jsx',
      './assets/js/apps/book_create/index.jsx',
      './assets/js/apps/book_review/index.jsx',
  ],

  output: {
      path: path.resolve('./assets/bundles/'),
      filename: '[name]-[hash].js',
      publicPath: 'http://localhost:3000/assets/bundles/', // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(), // don't reload if there is an error
    new BundleTracker({filename: './webpack-stats.json'}),
  ],

  module: {
    loaders: [
      // we pass the output from babel loader to react-hot loader
      { test: /\.jsx?$/, exclude: /node_modules/, loaders: ['react-hot', 'babel'], },
    ],
  },

  resolve: {
    modulesDirectories: ['node_modules'],
    extensions: ['', '.js', '.jsx'],
    modules: [
        path.join(__dirname, '/assets/js'),
        path.join(__dirname, '/node_modules'),
    ]
  },

  watch: false,

  watchOptions: {
    poll: 100,
  },

}
