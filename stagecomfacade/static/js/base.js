var heightheader = $("#header")
$(window).on("scroll",function(e){
    if($(window).scrollTop() >= (heightheader[0].clientHeight)/2){
        
        if(! heightheader[0].classList.contains("background")){
            heightheader[0].classList.add("background")
        }
    }else{
        if(heightheader[0].classList.contains("background")){
            heightheader[0].classList.remove("background")
        }
    }
})

$(window).on("load",function(e){
    if($(window).scrollTop() >= (heightheader[0].clientHeight)/2){
        
        if(! heightheader[0].classList.contains("background")){
            heightheader[0].classList.add("background")
        }
    }else{
        if(heightheader[0].classList.contains("background")){
            heightheader[0].classList.remove("background")
        }
    }
})


//scroll left 




if(document.getElementById("revscroll")){
    var listscrolleft= document.getElementById("revscroll");
    listscrolleft.style.left = 0;
    listscrolleft.style.transitionDuration ="0px"
}
  
    


    


