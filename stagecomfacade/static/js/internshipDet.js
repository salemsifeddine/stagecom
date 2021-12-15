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

wrapperparrent.addEventListener("click",function(){
    $(this).fadeOut(500)
        setTimeout(() => {
            wrapperDiv.style.transform = "translate(0,-25%)"
        }, 200);
})
wrapperDiv.addEventListener("click",function(e){
    e.preventDefault();
    e.stopPropagation()
})
