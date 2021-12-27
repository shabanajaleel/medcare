$(document).ready(function(){
    $("#dep-search").on("keyup", function() {
        
      var value = $(this).val().toLowerCase();
      $("#doctor-table tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
      $("#docappointment tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });
  