var assert = require('assert'),
    textToKeypad = require('./textToKeypad').textToKeypad;

// 'ABC'    : 2,
// 'DEF'    : 3,
// 'GHI'    : 4,
// 'JKL'    : 5,
// 'MNO'    : 6,
// 'PQRS'   : 7,
// 'TUV'    : 8,
// 'WXYZ'   : 9,
// ' '      : 0,

describe("textToKeypad", function () {
    it("1 char", function () {
        var message = 'A'
        var output = 2
        assert.equal(textToKeypad(message), output)
    })
    it("1 char.2", function () {
        var message = ' '
        var output = 0
        assert.equal(textToKeypad(message), output)
    })
    // Para ser possível obter duas letras sequenciais referenciadas pelo mesmo número, 
    // deve ser utilizado o caractere _ como separador.
    it("2 chars", function () {
        var message = 'AA'
        var output = '2_2'
        assert.equal(textToKeypad(message), output)
    })
    it("3 chars", function () {
        var message = 'AAA'
        var output = '2_2_2'
        assert.equal(textToKeypad(message), output)
    })
    it("3 chars.2", function () {
        var message = 'AAB'
        var output = '2_2_22'
        assert.equal(textToKeypad(message), output)
    })
    it("3 same chars", function () {
        var message = 'AAA'
        var output = '2_2_2'
        assert.equal(textToKeypad(message), output)
    })
    it("10 chars", function () {
        var message = 'AAAAAAAAAA'
        var output =   '2_2_2_2_2_2_2_2_2_2'
        assert.equal(textToKeypad(message), output)
    })
    it("LO", function () {
        // 555 666
        // L    O  
        var message = 'LO'
        var output = '555666'
        assert.equal(textToKeypad(message), output)
    })
    it("LOR", function () {
        // 555 666 777
        // L    O   R 
        var message = 'LOR'
        var output = '555666777'
        assert.equal(textToKeypad(message), output)
    })

    it("LOREM", function () {
        // 555 666 777 33 6 
        // L    O   R  E  M 
        var message = 'LOREM'
        var output = '555666777336'
        assert.equal(textToKeypad(message), output)
    })
    it("LOREM ", function () {
        // 555 666 777 33 6  0
        // L    O   R  E  M sp
        var message = 'LOREM '
        var output = '5556667773360'
        assert.equal(textToKeypad(message), output)
    })
    it("LOREM I", function () {
        // 555 666 777 33 6  0  444
        // L    O   R  E  M sp  I  
        var message = 'LOREM I'
        var output = '5556667773360444'
        assert.equal(textToKeypad(message), output)
    })
    it("Default test 2", function () {
        // 555 666 777 33 6  0  444 7_7777
        // L    O   R  E  M sp  I   P_S   
        var message = 'LOREM IPS'
        var output = '55566677733604447_7777'
        assert.equal(textToKeypad(message), output)
    })
    it("Default test 2", function () {
        // 555 666 777 33 6  0  444 7_7777 88 6
        // L    O   R  E  M sp  I   P_S    U  M
        var message = 'LOREM IPSUM'
        var output = '55566677733604447_7777886'
        assert.equal(textToKeypad(message), output)
    })
    it("Default test 2.1", function () {
        // 555 666 777 33 6  0  444 7_7777 88 6
        // L    O   R  E  M sp  I   P_S    U  M
        var message = 'LOREM IPSUM'
        var output = '55566677733604447_7777886'
        assert.equal(textToKeypad(message), output)
    })
    it("Default test 1", function () {
        var message = 'QUERO TRABALHAR NA ACTIVESALES'
        var output = '778833777666087772_22_2555442777066202_22284448883377772555337777'
        assert.equal(textToKeypad(message), output)
    })
})