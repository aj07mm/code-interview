var assert = require('assert'),
    scope = require('./scope').scope;

describe("scopeTest", function () {
    it("sumFn1", function () {
		assert.equal(scope.sumFn1(), 2)
    })
    it("sumFn2", function () {
		assert.equal(scope.sumFn2(), 4)
    })
})