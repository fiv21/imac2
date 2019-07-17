
$(document).ready(function(){
 
        $('table').on('mousedown', 'input', function(e){
      var id_seleccionado= $(this).attr('value');
      $("#id_pac_ergo").val(id_seleccionado);

  });

});