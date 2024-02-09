let ButtonDark_Light = document.getElementById('changecolourbutton');
const nume_item = "mode";

setInterval(checkMode, 0);

function checkMode() {
    if (window.localStorage.getItem(nume_item) == 'dark' || window.localStorage.getItem(nume_item) == null) turndark();
    else {
        turnlight();
    }
    clearInterval();
}

function turnlight() {
    document.documentElement.style.setProperty('--white', '#222525')
    document.documentElement.style.setProperty('--black', '#f8f5f2')
    document.documentElement.style.setProperty('--purple', '#078080')
    document.documentElement.style.setProperty('--grey', '#f45d48')
    document.documentElement.style.setProperty('--black2', '#f8f5a9')
}

function turndark() {
    document.documentElement.style.setProperty('--white', '#fffffe')
    document.documentElement.style.setProperty('--black', '#16161a')
    document.documentElement.style.setProperty('--purple', '#7f5af0')
    document.documentElement.style.setProperty('--grey', '#94a1b2')
    document.documentElement.style.setProperty('--black2', '#010101')
}

ButtonDark_Light.addEventListener("click", function () {
    if (window.localStorage.getItem(nume_item) == 'dark' || window.localStorage.getItem(nume_item) == null) {
        window.localStorage.clear();
        window.localStorage.setItem(nume_item, 'light')
        turnlight();
    } else {
        window.localStorage.removeItem(nume_item);
        turndark();
        window.localStorage.setItem(nume_item, 'dark');
    }
})

document.addEventListener('keydown', (e) => {
    switch (e.keyCode) {
        case 39:
            if (window.localStorage.getItem(nume_item) == 'dark' || window.localStorage.getItem(nume_item) == null) {
                window.localStorage.clear();
                window.localStorage.setItem(nume_item, 'light')
                turnlight();
            }
            break
        case 37:
            if (window.localStorage.getItem(nume_item) == 'light') {
                window.localStorage.removeItem(nume_item);
                turndark();
                window.localStorage.setItem(nume_item, 'dark');
            }
            break
    }
})

let changebuton = document.getElementById("changecolourbutton");
setInterval(schimbaCuloareaButonului, 2000);

function schimbaCuloareaButonului() {
    let culoareRandom = Math.floor(Math.random() * 16777215).toString(16);
    changebuton.style.backgroundColor = '#' + culoareRandom;
}