

if(document.getElementById("btnapply")){
    document.getElementById("btnapply") .addEventListener("click",function(){

        


        $(".wrapper-parent").fadeIn(500)
        setTimeout(() => {
            wrapperDiv.style.transform = "translate(0,0)"
            
        }, 200);
        var inputUserName = document.getElementById("usernameUser")
        var inputUserEmail = document.getElementById("EmailUser")
        var inputTextArea = document.getElementById("textareainput")
        setTimeout(() => {
            inputUserName.value = userNm111
            inputUserEmail.value = userEml11
            inputTextArea.addEventListener("keyup",function(){
                if(inputTextArea.value.length > 0 ){
                
                   this.nextElementSibling.style.display="none"
                }
                if(inputTextArea.value.length == 0 ){
                    this.nextElementSibling.style.display="block"
                }
            })
        }, 200);


       
    })
    
}




function InternshipApi(id, action){
    url="/internshipApi/"
    fetch(url,{
        method:"POST",
        headers:{
            "content-type":"application/json",
            "X-CSRFToken":csrftoken
        },
        body: JSON.stringify({
            "internshipId":id,
            "action":action,
            
        })
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        //
     console.log(data)
            //  location.reload()
        
       

        //
    })
}

if(document.querySelector('.save-internship') ){
    var savebtninternship = document.querySelector('.save-internship') 
    
savebtninternship.addEventListener("click",function(){

    this.classList.toggle("added")
    if(this.parentNode.classList[0] == "save-course"){
        var parentdivSave= this.parentNode
        parentdivSave.classList.toggle("saveinternship")
    }
    
    var wishinternship=this.dataset.internship 

    if(user == "AnonymousUser"){
        console.log('not logged')
    
    }else{
        if(this.classList.contains('added')){
            var styleele = document.createElement("style");
            var textStyle = document.createTextNode(".details-header .save-job::before{background:rgba(32, 26, 220, 0.3)}")
            styleele.appendChild(textStyle)
            document.head.appendChild(styleele)

            // this.innerHTML = `<i class="fas fa-heart"></i> Remove From WishList`
            InternshipApi(wishinternship,"addInternship")
    
        }else{
            var styleele = document.createElement("style");
            var textStyle = document.createTextNode(".details-header .save-job::before{background:rgba(255, 255, 255, 0.3)}")
            styleele.appendChild(textStyle)
            document.head.appendChild(styleele)
            // this.innerHTML = `<i class="far fa-heart"></i> Add To WishList`
            InternshipApi(wishinternship,"removeInternship")
    
        }

    
    }
    



})

}



// 
$("#file-upload").css("opacity", "0");

$("#file-browser").click(function(e) {
  e.preventDefault();
  $("#file-upload").trigger("click");
});

document.getElementById("file-browser").addEventListener("click",function(){
    document.getElementById("fileuploadImageBack").click()
})

// great form 


function init(count) {
    // Generate li foreach fieldset
    for (var iii= 0; iii < count; iii++){
        var li = document.createElement("li");
  
        document.querySelector('.items').appendChild(li);
    }
    // Add class active on first li
    document.querySelector('.items').children[0].classList.add('active');

  }
  
  function next(target) {
    var input = target.previousElementSibling;
    
    // Check if input is empty
    if (input.value === '') {
      document.querySelector(".form-internship").classList.add('error');
    } else {
        document.querySelector(".form-internship").classList.remove('error');
      
      var enable = document.querySelector('form fieldset.enable'),
          nextEnable = enable.nextElementSibling;
      enable.classList.remove('enable');
      enable.classList.add('disable');
      nextEnable.classList.add('enable');
      
      // Switch active class on left list
      var active = document.querySelector('ul.items li.active'),
          nextActive = active.nextElementSibling;
      active.classList.remove('active');
      nextActive.classList.add('active');
    }
  }
  
  function keyDown(event) {
    var key = event.keyCode,
        target = document.querySelector('fieldset.enable .buttondown');
    if (key == 13 || key == 9) next(target);
  }
  
  var body = document.querySelector('body'),
      form = document.querySelector('.form-internship form'),
      count = form.querySelectorAll('fieldset').length;
      var ul = document.querySelector('.items')
      
    //  

    window.addEventListener("load",function(){
        init(count);
        
    })
 


  document.body.onmouseup = function (event) {
      var target = event.target || event.toElement;
      if (target.classList.contains("buttondown")) next(target);
  };
  document.addEventListener("keydown", keyDown, false);
  
  
// on click on br 
document.querySelector(".br").addEventListener("click",function(){
    $(".form-internship").fadeIn(150)
    $(".form-internship").animate({"height":100 + "vh"},500)
    $(".form-internship form").fadeIn(600)
})

document.querySelector(".form-internship").addEventListener("click",function(){
    // $(".form-internship form").animate({"width":0,"height":0},300)
    // $(".form-internship").animate({"width":0 + "%"},500)
    $(".form-internship").animate({"height":0 + "vh"},300)
    $(".form-internship form").hide(200)
    $(".form-internship").fadeOut(300)
    
})

document.querySelector(".form-internship form").addEventListener("click",function(e){
    
    e.stopPropagation();
    
})

function ajaxrequest(){
    majorF=document.querySelector(".major")
    placeF=document.querySelector(".place")
    countryF=document.querySelector(".tag")
    $.ajax({
        type:"get",
        url: "/ajaxreq/",
        data: {
                 'major': majorF.value,
                 'place': placeF.value,
                 'tag': countryF.value
               },
        success: function(data) {
            console.log(data)
           
           
            
                },
        error: function(){
                console.log("error");
             }
        });
}

document.querySelector(".marginbtm10").addEventListener("click",function(e){
    e.preventDefault();
    ajaxrequest();
})