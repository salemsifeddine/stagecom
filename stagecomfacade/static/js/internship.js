

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
            searchInternship(data);
           
            
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

// function to render searched internship
function searchInternship(data){
    var rowcourses = document.querySelector(".rowcrss")
    rowcourses.innerHTML=''
    var intsh=data.internships;
    for(var iin =0; iin < intsh.length; iin++){
        // create div with class name course
        var courseDiv= document.createElement("div")
        courseDiv.classList.add("course")
        // img course div with class named imgcourse
        var imgcourseDiv=document.createElement("div")
        imgcourseDiv.classList.add("imgcourse")
        // infocourse div with class named infocourse
        var infocourseDiv=document.createElement("div")
        infocourseDiv.classList.add("infocourse")
        // div with class named enroll-price
        var EnrollPriceDiv=document.createElement("div")
        EnrollPriceDiv.classList.add("enroll-price")
        // create imgEle
        var imgEle = document.createElement("img")
        imgEle.src="../static" + intsh[iin].image
        // append imgELe to parrentImg
        imgcourseDiv.appendChild(imgEle)
        var levelCourse= document.createElement("div")
        levelCourse.classList.add("course-level")
        var saveCourse=document.createElement("div")
        saveCourse.classList.add("save-course")
        var titleCourse=document.createElement("div")
        titleCourse.classList.add("title-course")
        var descCourse=document.createElement("div")
        descCourse.classList.add("desc")
        var h4ele = document.createElement("h4")
        var pEle = document.createElement("p")
        // cretae i ele 
        var iEle =document.createElement("i")
        iEle.classList.add("lni")
        iEle.classList.add("lni-bookmark")
        iEle.classList.add("save-internship")
        if(intsh[iin].exist){
            iEle.classList.add("added")
            saveCourse.classList.add("saveinternship")
            // var styleele = document.createElement("style");
            // var textStyle = document.createTextNode(".details-header .save-job::before{background:rgba(32, 26, 220, 0.3)}")
            // styleele.appendChild(textStyle)
            // document.head.appendChild(styleele)
        }else{
            console.log(intsh[iin].exist)
        }
        iEle.dataset.internship = intsh[iin].id

        var divbtn = document.createElement("div")
        var buttonanchor = document.createElement("a")
        divbtn.classList.add("apply-btn")
        buttonanchor.classList.add("button") 
        buttonanchor.classList.add("button-apply")
        buttonanchor.href="/internshipDet/" + intsh[iin].id
        
        // append text nodes for the last 4 divs
        var levelText =document.createTextNode(intsh[iin].level)
        var titleText =document.createTextNode(intsh[iin].title)
        var descText = document.createTextNode(intsh[iin].description)
        var buttonText = document.createTextNode("View Details")

        buttonanchor.appendChild(buttonText)
        divbtn.appendChild(buttonanchor)
        levelCourse.appendChild(levelText)
        h4ele.appendChild(titleText)
        titleCourse.appendChild(h4ele)
        pEle.appendChild(descText)
        descCourse.appendChild(pEle)
        saveCourse.appendChild(iEle)
        EnrollPriceDiv.appendChild(divbtn)
        // 
        infocourseDiv.appendChild(levelCourse)
        infocourseDiv.appendChild(saveCourse)
        infocourseDiv.appendChild(titleCourse)
        infocourseDiv.appendChild(descCourse)


        // 
        courseDiv.appendChild(imgcourseDiv)
        courseDiv.appendChild(infocourseDiv)
        courseDiv.appendChild(EnrollPriceDiv)
        
        
        rowcourses.appendChild(courseDiv)

        // 
        document.querySelectorAll('.save-internship').forEach(ele=>
            ele.addEventListener("click",function(){
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
        )
    }
    
}





// 
if(document.querySelector('.save-internship') ){
    var savebtninternship = document.querySelectorAll('.save-internship') 
    
savebtninternship.forEach(ele =>
    ele.addEventListener("click",function(){

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
)
}