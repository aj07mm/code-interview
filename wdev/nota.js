// Você pode corrigir o código abaixo para que passe nos testes?
// getNotaFiscal(1234, getItensNotaFiscal);
getNotaFiscal(1234, function(notaFiscal){
	console.log(notaFiscal)
	getItensNotaFiscal(notaFiscal, function(itens){

	})
});
setTimeout(function() {
	console.log(foo)
  // assert(notaFiscal, "Nota fiscal encontrada");
  // assert(notaFiscal.numero === 1234, "Número da nota fiscal correto");
  // assert(itens, "Itens encontrados");
  // assert(itens.length === 3, "Número de itens correto");
}, 1000);


// O CÓDIGO ABAIXO NÃO PODE SER MODIFICADO
// ============================================
// FUNÇÕES DE APOIO
function getNotaFiscal(numero, cb) {
    setTimeout(function() { cb && cb({ numero: numero });
    }, 100);
}

function getItensNotaFiscal(notaFiscal, cb) {
    setTimeout(function() {
        var itens = [];
        if(notaFiscal && notaFiscal.numero === 1234) {
            for(var i = 1; i < 4; i++) {
                itens.push({ item: i, descricao: "Item " + i });
            }
        }
        cb && cb(itens);
    }, 100);
}