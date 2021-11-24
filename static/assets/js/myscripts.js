var main_detail = $(".image-holder")
var image_holder = $("#image_holder")
var bio_holder = $("#bio")
var master_skill_holder = $("#master_skill")
var proficient_skill_holder = $("#proficient_skill")
var future_skill_holder = $("#future_skill")
var learning_skill_holder = $("#learning_skill")
var related_user_holder = $("#related_user")
var pathname = window.location.pathname;
const id = pathname.match(/\d+/)[0]

var image_html = `<img src={{image_url}} class="img-fluid rounded-start" alt="...">`;
var bio_html = `<h5 class="card-title text-center">{{first_name}} {{last_name}}</h5></div>
                <p class="card-text"><h6>Contact</h6></p>
                  <p class="card-text"><small class="text-muted">{{email}}</small></p></div>`;
var master_skill_html = `Master:<ul style="list-style-type: none;">{{#skills}}  {{#master}}<li><button id={{title}} class="btn btn-secondary btn-sm skill_btn">{{title}} </li></button>{{/master}} {{/skills}} </ul>`;
var proficient_skill_html = `Proficient:<ul style="list-style-type: none;">{{#skills}}  {{#proficient}}<li><button id={{title}} class="btn btn-secondary btn-sm skill_btn" onclick="myFunction(this.id)">{{title}}</button> </li>{{/proficient}} {{/skills}} </ul>`;
var learning_skill_html = `Currently Learning:<ul style="list-style-type: none;">{{#skills}}  {{#learning}}<li><button id={{title}} class="btn btn-secondary btn-sm skill_btn">{{title}}</button> </li>{{/learning}} {{/skills}} </ul>`;
var future_skill_html = `Hope to Learn:<ul style="list-style-type: none;">{{#skills}}  {{#future}}<li><button id={{title}} class="btn btn-secondary btn-sm skill_btn">{{title}}</button> </li>{{/future}} {{/skills}} </ul>`;
var related_user_html = `<div class="col-sm-4" >

       <div class="card" style="width: 18rem;">
                  <img src={{image_url}} class="card-img-top" alt="...">
                  <div class="card-body">
                    <h5 class="card-title text-center">{{first_name}} {{last_name}}</h5>
                    <p class="card-text text-center">{{current_role}}</p>
                  </div>
                  <ul class="list-group list-group-flush">
                    {{#skills}}<li class="list-group-item"> {{title}} </li>{{/skills}}
                  </ul>
                </div>  </div>`

function appendUser(user){
    related_user_holder.append(Mustache.render(related_user_html, user))
}
function myFunction(title) {
event.preventDefault();
    console.log(title);
     $.ajax({
        type:'GET',
        url: '/account/related/'+ title,
        success: function(users){
            $.each(users, function(i, user){
                appendUser(user)
            })
        }
    });
}

function renderImage(user){
    image_holder.append(Mustache.render(image_html, user));
}

function renderBio(user){
    bio_holder.append(Mustache.render(bio_html, user));
}

function renderMasterSkills(user){
    master_skill_holder.append(Mustache.render(master_skill_html, user));
}

function renderProficientSkills(user){
    master_skill_holder.append(Mustache.render(proficient_skill_html, user));
}

function renderLearningSkills(user){
    master_skill_holder.append(Mustache.render(learning_skill_html, user));
}

function renderFutureSkills(user){
    master_skill_holder.append(Mustache.render(future_skill_html, user));
}



$(function(){
    $.ajax({
        type:'GET',
        url: '/account/mydetail/'+ id,
        success: function(data){
            renderImage(data);
            renderBio(data);
            renderMasterSkills(data);
            renderProficientSkills(data);
            renderLearningSkills(data);
            renderFutureSkills(data);
        }
    });
})