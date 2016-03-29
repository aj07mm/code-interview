//função textToKeypad de forma que dada uma mensagem de texto limitada a 255 caracteres, 
//retorne a sequência de números que precisa ser digitada.

String.prototype.repeat = function( num ){
    return new Array( num + 1 ).join( this );
}

exports.textToKeypad = function (text) {
    var res = [];
    var lastButton = ''
    for (var i = 0; i <= text.length - 1; i++) {
        currentButton = getButton(text[i]);
        if(lastButton == currentButton){
            res.push('_');
        }
        res.push(getNumByButton(currentButton).toString().repeat(currentButton.indexOf(text[i]) + 1));
        lastButton = currentButton;
    };
    return res.join('');
}

var getDicKeyboard = function(){
    return {
        'ABC'    : 2,
        'DEF'    : 3,
        'GHI'    : 4,
        'JKL'    : 5,
        'MNO'    : 6,
        'PQRS'   : 7,
        'TUV'    : 8,
        'WXYZ'   : 9,
        ' '      : 0,
    };
}

var getButton = function(char){
    var res = '';
    for(chars in getDicKeyboard()){
        var pos = chars.indexOf(char);
        if(pos != -1){
            return chars
        }
    }
}

var getNumByButton = function(button){
    return getDicKeyboard()[button]
}
