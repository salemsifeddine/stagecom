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