const inputs = document.querySelectorAll('input');

inputs.forEach(el => {
  el.addEventListener('blur', e => {
    if(e.target.value) {
      e.target.classList.add('dirty');
    } else {
      e.target.classList.remove('dirty');
    }
  })
})


var studentReg = document.getElementById("studentReg")
var companyReg = document.getElementById("companyReg")



studentReg.addEventListener("change",function(){
    if(this.checked && companyReg.checked){
      this.checked=true
      this.dataset.value = "True"
      companyReg.checked = false
      companyReg.dataset.value= "False"
    }
})

companyReg.addEventListener("change",function(){
  if(this.checked && studentReg.checked){
    this.checked=true
    this.dataset.value="True"
    studentReg.checked = false
    studentReg.dataset.value="False"
  }
})

