# coalitionjob

#####database config:

	'mysql' => [
	    'driver'    => 'mysql',
	    'host'      => env('DB_HOST', 'localhost'),
	    'unix_socket'   => '/tmp/mysql.sock',
	    'database'  => env('DB_DATABASE', 'coalition'),
	    'username'  => env('DB_USERNAME', 'root'),
	    'password'  => env('DB_PASSWORD', ''),
	    'charset'   => 'utf8',
	    'collation' => 'utf8_unicode_ci',
	    'prefix'    => '',
	    'strict'    => false,
	],

#####How to run:

Configurate the database
run migrations
	php artisan migrate
and up the server
	php artisan serve