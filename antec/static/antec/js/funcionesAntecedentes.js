/**************************Selecion de Id Paciente***************************/

$(document).ready(function(){    
      	$('table').on('mousedown', 'input', function(e){
    	var id_seleccionado= $(this).attr('value');
		$("#id_pac_antec").val(id_seleccionado);
	});
});
