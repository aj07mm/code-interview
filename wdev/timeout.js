var resultados = [];
// for ( var i = 0; i <= 3; i++ ) {
for ( var i = 60; i <= 63; i++ ) {
    setTimeout(function(){
        // Não altere a linha abaixo
    	resultados.push(String.fromCharCode(65 + i));
    }, i * 1300);    
}
console.log(resultados)