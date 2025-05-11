let menu = document.querySelector(".menu")
let aside = document.querySelector(".side-navbar")

isToggle = true

menu.addEventListener('click', ()=>{
    if(isToggle){
        aside.style.display = "flex"
        isToggle = false
    }else{
        aside.style.display = "none"
        isToggle = true
    }
    
})