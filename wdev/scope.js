// Dada as duas operações abaixo, capturamos as funções de execução e validamos os resultados,
// porém por algum motivo os testes das funções não passaram.
// NÃO MODIFIQUE A LINHA ABAIXO
var op1 = new SumOperation(1, 1), 
	op2 = new SumOperation(2, 2);


// Alterando as duas linhas abaixo, você consegue corrigir o problema sem criar utilizar a instrução "function" ou arrow function? 

var sumFn2 = op2.execute;

//_val1 = 1 e _val2 =2  pertencem ao objeto op1
// console.log(op1.execute()) // 2 

//nao tem _val1 nem _val2
// var sumFn1 = op1.execute;
// var sumFn2 = op2.execute;


var sumFn1 = op1.execute.bind({
    _val1 : 1,
    _val2 : 1
})

var sumFn2 = op2.execute.bind({
    _val1 : 2,
    _val2 : 2
})


// ============================================
// O CÓDIGO ABAIXO NÃO PODE SER MODIFICADO


// FUNÇÕES DE APOIO
function SumOperation(val1, val2) {
    this._val1 = val1;
    this._val2 = val2;
    this.execute = function execute() {
	    return this._val1 + this._val2;
	};
}

exports.scope = {
    sumFn1 : sumFn1,
    sumFn2 : sumFn2
}