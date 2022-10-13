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