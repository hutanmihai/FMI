let divDataConectare = document.getElementById("data-conectarii");
let dataconectare = window.localStorage.getItem("data-conectare");
divDataConectare.innerText = dataconectare;

document.getElementById('email-conectat').innerText = window.sessionStorage.getItem('email');

document.getElementById('parola-curenta').innerText = window.sessionStorage.getItem('password');

document.getElementById('changepassword').addEventListener('click', (e) => {
    const email = window.sessionStorage.getItem('email');
    const password = window.sessionStorage.getItem('password');
    fetch(`/change-password?email=${email}&password=${password}`, {
        method: "PUT",
    }).then((res) => {
        return res.json()
    })
        .then((data) => {
            window.sessionStorage.setItem('password', data.parolanoua);
            window.location.href = '../myaccount'
        })
})

document.getElementById('deleteaccount').addEventListener('click', (e) => {
    const email = window.sessionStorage.getItem('email');
    const password = window.sessionStorage.getItem('password');
    fetch(`/delete-account?email=${email}&password=${password}`, {
        method: "DELETE"
    }).then((res) => {
        if (res.ok) {
            window.sessionStorage.clear();
            window.location.href = "../";
        }
    })
})