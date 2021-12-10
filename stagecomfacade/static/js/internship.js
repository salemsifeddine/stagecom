var wrapperparrent = document.querySelector(".wrapper-parent");

var wrapperDiv = document.getElementById("wrapperdiv")
if(document.querySelector(".concelbtn")){
    var concelbtn = document.querySelector(".concelbtn");
    

    concelbtn.addEventListener("click",function(e){
        

    
        $(".wrapper-parent").fadeOut(500)
        setTimeout(() => {
            wrapperDiv.style.transform = "translate(0,-25%)"
        }, 200);
        
        

    })

}




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

