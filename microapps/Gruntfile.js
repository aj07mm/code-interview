module.exports = function(grunt) {
	grunt.initConfig({
	  // babel: {
	  //    options: {
	  //        sourceMap: true,
	  //        presets: ['es2015']
	  //    },
	  //    dist: {
	  //        files: {
	  //        	'www/js/app.js': 'www/js/es2015/app.js'
	  //        }
	  //    }
	  // },
	  uglify: {
	    files: {
	      src: [
	      	'bower_components/angular/angular.js',
	      	'bower_components/sweetalert/dist/sweetalert.min.js',
	      	'www/js/*.js'
	      ],
	      dest: 'build/index.min.js',
	      options: {
			report: 'min',
			mangle: false
		  }
	    }
	  },
	  watch: {
	    js:  { files: 'www/js/*.js', tasks: [ 'uglify' ] },
	  },
	  cssmin: {
		  options: {
		    shorthandCompacting: false,
		    roundingPrecision: -1
		  },
		  target: {
		    files: {
		      'build/index.css': [
		      	'www/css/*.css',
		      	'bower_components/skeleton/css/normalize.css',
		      	'bower_components/skeleton/css/skeleton.css',
		      	'bower_components/Ionicons/css/ionicons.min.css',
		      	'bower_components/sweetalert/dist/sweetalert.css'
		      ]
		    }
		  }
	  }
	});

	// load plugins
	// grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-uglify');
	grunt.loadNpmTasks('grunt-contrib-cssmin');

	// register at least this one task
	grunt.registerTask('default', [ 'uglify', 'cssmin' ]);
};