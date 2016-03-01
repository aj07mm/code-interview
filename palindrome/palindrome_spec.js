var assert = require ('assert'),
    palindrome = require('./palindrome').palindrome;

describe('palindrome', function() {
    it('aba', function () {
        var word = 'aba'
        assert.equal(palindrome(word), true)
    })
    it('abba', function () {
        var word = 'abba'
        assert.equal(palindrome(word), true)
    })
    it('xxx', function () {
        var word = 'xxx'
        assert.equal(palindrome(word), true)
    })
    it('abdc', function () {
        var word = 'abdc'
        assert.equal(palindrome(word), false)
    })
})