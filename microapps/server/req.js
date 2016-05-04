var http = require('https');
var express = require('express');
var querystring = require('querystring');
var app = express();
var bodyParser = require('body-parser')
var cors = require('cors')

function request(data, callback) {
	var path='/v1/checkouts';
	var data = querystring.stringify(data);
	var options = {
		port: 443,
		host: 'test.oppwa.com',
		path: path,
		method: 'POST',
		headers: {
			'Content-Type': 'application/x-www-form-urlencoded',
			'Content-Length': data.length
		}
	};
	var postRequest = http.request(options, function(res) {
		res.setEncoding('utf8');
		res.on('data', function (chunk) {
			jsonRes = JSON.parse(chunk);
			return callback(jsonRes);
		});
	});
	console.log(data)
	postRequest.write(data);
	postRequest.end();
}

app.use(bodyParser.json())
app.use(cors())

app.post('/checkout', function(req, res){
	console.log(req.body)
	var data = {
		'authentication.userId' : req.body['authentication']['userId'],
		'authentication.password' : req.body['authentication']['password'],
		'authentication.entityId' : req.body['authentication']['entityId'],
		'amount' : req.body['amount'],
		'currency' : req.body['currency'],
		'paymentType' : req.body['paymentType']
	};
	request(data, function(paymentRes){
		res.send({
			"response": paymentRes
		});
	});
});

app.listen(3000);