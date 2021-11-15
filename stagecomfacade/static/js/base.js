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




var listscrolleft= document.getElementById("revscroll");
  
    
var scrolleftrev = setInterval(() => {
    listscrolleft.style.left = 0;
    listscrolleft.style.transitionDuration ="0px"
    
}, 1000);

