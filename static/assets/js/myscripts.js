var main_detail = $('#main_detail')
$(function(){
    $.ajax({
        type:'GET',
        url: '/account/mydetail/2',
        success: function(data){

            main_detail.append(
                `<div class="card main_detail">
                  <img src=${data.image_url} alt="Avatar" style="width:100%">
                  <div class="container">
                    <h4><b>${data.email}</b></h4>
                    <p>Architect & Engineer</p>
                  </div>
                </div>`
            )
        }
    });
})