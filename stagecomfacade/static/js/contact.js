
inputTextArea = document.getElementById("textareainput")

inputTextArea.addEventListener("keyup",function(){
    if(inputTextArea.value.length > 0 ){
    
       this.nextElementSibling.style.display="none"
    }
    if(inputTextArea.value.length == 0 ){
        this.nextElementSibling.style.display="block"
    }
})