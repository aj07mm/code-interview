exports.each = function(list, callback) {
	list.map(function(num){
		callback(num++)
	});
}