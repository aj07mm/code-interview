var Promise = require("bluebird");

getNotaFiscal(1234).then(function(notaFiscal){
	assert(notaFiscal, "Nota fiscal encontrada");
	assert(notaFiscal.numero === 1234, "Número da nota fiscal correto");
	return notaFiscal
}).then(getItensNotaFiscal).then(function(itens){
	console.log(itens)
})

function getNotaFiscal(numero, cb) {
	return new Promise(function (resolve, reject) {
		setTimeout(function() {
	        resolve({ numero: numero })
	    }, 100);
    });
}

function getItensNotaFiscal(notaFiscal, cb) {
	return new Promise(function (resolve, reject) {
		setTimeout(function() {
	        var itens = [];
	        if(notaFiscal && notaFiscal.numero === 1234) {
	            for(var i = 1; i < 4; i++) {
	                itens.push({ item: i, descricao: "Item " + i });
	            }
	        }
	        resolve(itens);
	    }, 100);
	});
}