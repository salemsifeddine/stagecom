var wrapperparrent = document.querySelector(".wrapper-parent");
var wrapperDiv = document.getElementById("wrapperdiv")


document.getElementById("btnapply").addEventListener("click",function(){
    wrapperparrent.style.display= "block"
    wrapperparrent.style.opacity = 1
    setTimeout(() => {
        wrapperDiv.style.transform = "translate(0,0)"
    }, 200);

})