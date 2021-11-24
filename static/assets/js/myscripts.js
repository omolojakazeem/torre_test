var main_detail = $(".image-holder")
var image_holder = $("#image_holder")
var bio_holder = $("#bio")
var master_skill_holder = $("#master_skill")
var proficient_skill_holder = $("#proficient_skill")
var future_skill_holder = $("#future_skill")
var learning_skill_holder = $("#learning_skill")
var pathname = window.location.pathname;
const id = pathname.match(/\d+/)[0]

var image_html = `<img src={{image_url}} class="img-fluid rounded-start" alt="...">`;
var bio_html = `<h5 class="card-title text-center">{{first_name}} {{last_name}}</h5></div>
                <p class="card-text"><h6>Contact</h6></p>
                  <p class="card-text"><small class="text-muted">{{email}}</small></p></div>`;
var master_skill_html = `Master:<ul style="list-style-type: none;">{{#skills}}  {{#master}}<li>{{title}} </li>{{/master}} {{/skills}} </ul>`;
var proficient_skill_html = `Proficient:<ul style="list-style-type: none;">{{#skills}}  {{#proficient}}<li>{{title}} </li>{{/proficient}} {{/skills}} </ul>`;
var learning_skill_html = `Currently Learning:<ul style="list-style-type: none;">{{#skills}}  {{#learning}}<li>{{title}} </li>{{/learning}} {{/skills}} </ul>`;
var future_skill_html = `Hope to Learn:<ul style="list-style-type: none;">{{#skills}}  {{#future}}<li>{{title}} </li>{{/future}} {{/skills}} </ul>`;


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