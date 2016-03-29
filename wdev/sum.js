// Dada as duas operações abaixo, capturamos as funções de execução e validamos os resultados,
// porém por algum motivo os testes das funções não passaram.
// NÃO MODIFIQUE A LINHA ABAIXO
// var op1 = new SumOperation(1, 1), op2 = new SumOperation(2, 2);


// Alterando as duas linhas abaixo, você consegue corrigir o problema sem criar utilizar a instrução "function" ou arrow function? 
// var sumFn1 = op1.execute;
// var sumFn2 = op2.execute;
// console.log(op1.execute())
// console.log(op2.execute())


// console.log(SumOperation(1,1))
var op1 = new SumOperation(1, 1), op2 = new SumOperation(2, 2);
//ele executa, mas se passar pra outro nao vai, só ele pode executar depois de instanciado
// console.log(op1.execute())
//nao vai
// var sumFn1 = op1.execute;
// console.log(sumFn1())

// var sumFn1 = new SumOperation(1, 1); //objeto com props
// console.log(sumFn1.execute()) // nao me retorna porque esse nao é mais o objeto com as props
// foo = sumFn1

// console.log(op1._val1, new SumOperation(op1._val1, op1._val2)) // só posso pegar o valor no objeto
console.log(Object.call('execute', op1))
// sumFn1.prototype = new SumOperation(op1._val1, op1._val2)
// console.log(op1.execute)


// TESTES
// assert(sumFn1() == 2, 'Valor esperado: 2, recebido:' + sumFn1());
// assert(sumFn2() == 4, 'Valor esperado: 4, recebido:' + sumFn2());

// FUNÇÕES DE APOIO
function SumOperation(val1, val2) {
    this._val1 = val1;
    this._val2 = val2;
    this.execute = function execute() {
	    return this._val1 + this._val2;
	};
}