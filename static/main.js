$( document ).ready(function() {
    var i;
    for (i = 0; i < $('#pcc').children().length; i++) {
    $('#pcc').children().eq(i).attr('id','pc'+i)
    $('#bcps').children().eq(i).attr('id','bcp'+i)
    $('#inp').children().eq(i).attr('id','inpu'+i)
    $('#tos').children().eq(i).attr('id','tos'+i);
    $('#tsp').children().eq(i).attr('id','tsp'+i);
    $('#fly').children().eq(i).attr('id','fly'+i);
     var bcp_input=parseFloat($('#bcps').children('td').eq(i).html());
       var tos=parseFloat($('#tos').children('td').eq(i).html());
       var tsp=parseFloat(bcp_input+tos);
      // console.log($('#bcps >td > #bcp'+(i+1)).html('ll'));
       $('#tsp').children('td').eq(i).html(tsp);
       var input_Flyer=parseFloat(tsp/0.6).toFixed(2);
       $('#fly').children('td').eq(i).html(input_Flyer);
     }

$(".tgp").change(function(){
var id = $(this).closest('td').attr('id');
var value = $(this).val();
var nid =  id.split('u')[1]
var chg_val = $('#pc'+nid).html(); 
var set_val = chg_val/(1-(value/100)); 
$('#bcp'+nid).html(set_val.toFixed(2));
for (i = 0; i < $('#pcc').children().length; i++) {
calc_total(i);
var bcp_input=parseFloat($('#bcps').children('td').eq(i).html());
var tos=parseFloat($('#tos').children('td').eq(i).html());
var tsp=parseFloat(bcp_input+tos).toFixed(2);
$('#tsp').children('td').eq(i).html(tsp);
var input_Flyer=parseFloat(tsp/0.6).toFixed(2);
$('#fly').children('td').eq(i).html(input_Flyer);
}
});
$('#mrk').change(function(){
$('.'+$('select.ddlopt').attr('class')).each(function(i){
     for (i = 0; i < $(this).parents('.optval').find('.tdopt').length; i++) {
        if($(this).val()=='Y'){
             var new_val = parseFloat($(this).prev().val()*(1+($('#mrk').val()/100))).toFixed(2);
             $(this).parents('.optval').children('td').eq(i).html(new_val);
        }
        calc_total(i);
        var bcp_input=parseFloat($('#bcps').children('td').eq(i).html());
        var tos=parseFloat($('#tos').children('td').eq(i).html());
        var tsp=parseFloat(bcp_input+tos).toFixed(2);
        $('#tsp').children('td').eq(i).html(tsp);
        var input_Flyer=parseFloat(tsp/0.6).toFixed(2);
        $('#fly').children('td').eq(i).html(input_Flyer);
     }
  });
});
    
$('.optcls').change(function(){
var parent = $(this).closest('tr');
    var inpval=$(this).val();
     var ddl =$(this).next().val();

    for (i = 0; i < $(this).parents('.optval').find('.tdopt').length; i++) {
       $(this).parents('.optval').children('td').eq(i).attr('id','tdopt'+i)
       if(ddl=='Y'){
            var new_val = parseFloat(inpval*(1+($('#mrk').val()/100))).toFixed(2);
            $('#tdopt'+i).html(new_val);
            $('.total',parent).text(new_val);
            calc_total(i);
            var bcp_input=parseFloat($('#bcps').children('td').eq(i).html());
            var tos=parseFloat($('#tos').children('td').eq(i).html());
            var tsp=parseFloat(bcp_input+tos).toFixed(2);
           $('#tsp').children('td').eq(i).html(tsp);
           var input_Flyer=parseFloat(tsp/0.6).toFixed(2);
           $('#fly').children('td').eq(i).html(input_Flyer);
       }
       $('#tdopt'+i).removeAttr("id");

    }

})
$('.ddlopt').change(function(){
var ddl=$(this).val();
    //console.log($("#opt +i option[value= " + $(this).val() + "]").attr("selected", "selected"));
    //var option = $('option:selected', this).attr('value');
    // $(".ddlopt option[value= " + this.value + "]").attr("selected", "selected");
    var inpval =$(this).prev().val();
    for (i = 0; i < $(this).parents('.optval').find('.tdopt').length; i++) {
       $(this).parents('.optval').children('td').eq(i).attr('id','tdopt'+i);
       if(ddl=='Y'){
            var new_val = parseFloat(inpval*(1+($('#mrk').val()/100))).toFixed(2);
            $('#tdopt'+i).html(new_val);
       }
       else{
       $('#tdopt'+i).html(0);
       }
       calc_total(i);
       var bcp_input=parseFloat($('#bcps').children('td').eq(i).html());
       var tos=parseFloat($('#tos').children('td').eq(i).html());
       var tsp=parseFloat(bcp_input+tos).toFixed(2);
       $('#tsp').children('td').eq(i).html(tsp);
       var input_Flyer=parseFloat(tsp/0.6).toFixed(2);
       $('#fly').children('td').eq(i).html(input_Flyer);
       $('#tdopt'+i).removeAttr("id");
    }
})
function calc_total(index) {
    var total = 0;
    $('table .optval').each(function() {
  //  console.log($('td', this).eq(index).length);
        var value = parseFloat($('td', this).eq(index).text());
        if (!isNaN(value)) {
            total += value;
        }
    });
    $('#tos').children('td').eq(index).text(total.toFixed(2));
}


});