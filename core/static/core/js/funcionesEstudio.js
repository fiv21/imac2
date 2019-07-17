
    function calcular(){
    masa=$('#num1').val(); // selecciona id y le pasa el valor a la variable masa
    if (masa== '') masa=0; // si no hay nada en el text asigna el valor 0
    talla=$('#num2').val();
    if (talla== '') talla=0;

/************** calculo de Indice de masa corporal(IMC) *******************/
metro=(talla/100);
metro2=metro*metro;
total=parseFloat(masa/metro2).toFixed(1); // tofixed(1) para redondear al primer decimal
$('#resultado').val(total); 

/************** calculo de superficie corporal *******************/

total= Math.sqrt((talla*masa)/3600); // tofixed(1) para redondear al primer decimal
total=parseFloat(total).toFixed(1);
$('#resultado2').val(total); 

}


$(document).ready(function(){


      
        $('table').on('mousedown', 'input', function(e){
    var id_seleccionado= $(this).attr('value');
    var edad_seleccionada= $(this).attr('id');
    // alert(edad_seleccionada);
    $("#id_pac_estudio").val(id_seleccionado);
    // alert(id_seleccionado); 
     // var año = edad_seleccionada.substr(9);
    var año = edad_seleccionada.slice(-5); // obtengo los ultimos cuatro valores de la cadena
     // alert(año);
    var añoInt= parseInt(año);
    // alert(2019 -añoInt);
    /*Obtengo año actual*/
    var fecha = new Date();
    var añoActual = fecha.getFullYear();
    // alert('El año actual es: '+ano);
    var edadPac= añoActual-añoInt;
    // alert(edadPac);
     $("#edad").val(edadPac);




});

});


