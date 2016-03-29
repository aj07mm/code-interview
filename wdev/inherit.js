function Base ( ) {
 this.color = "blue";
}

function Sub ( ) {

}
Sub.prototype = new Base( );
Sub.prototype.showColor = function ( ) {
 console.log( this.color );
}

var instance = new Sub ( );
instance.showColor( ); //"blue"