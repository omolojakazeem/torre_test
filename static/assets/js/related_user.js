
window.onload = function() {
    $(".skill_btn").click(function(){

    });

};


$(function(){
    $.ajax({
        type:'GET',
        url: '/account/related/'+ id,
        success: function(data){
            console.log(data)
        }
    });
})