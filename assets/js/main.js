let select = document.getElementById("access-option");
let input = document.getElementById("access-input");

select.addEventListener("change", accessInput);

function accessInput() {
    input.placeholder = this.value;
    if (this.value == "Acessar conta com") {
        input.setAttribute("disabled", "disabled");
    } else {
        input.removeAttribute("disabled");
    }
}

let closeMenuButton = document.getElementById("close-menu");
let menuUI = document.getElementById("menu");

closeMenuButton.addEventListener("click", closeOpenMenu);

function closeOpenMenu() {
    menuUI.classList.contains('hide')?menuUI.classList.remove('hide'):menuUI.classList.add('hide');
    
}