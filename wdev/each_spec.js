var assert = require('assert'),
    each = require('./each').each;

describe("each", function () {
    it("1 char", function () {
    	var output_incrementer = 0
		each([0, 1, 2], function(numero){
			assert.equal(numero, output_incrementer++)
		});
    })
})