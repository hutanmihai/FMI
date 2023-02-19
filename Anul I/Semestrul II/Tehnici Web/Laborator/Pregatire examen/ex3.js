const { METHODS } = require("http");

document.getElementById('button').addEventListener('click', (e) => {
    let numar = document.getElementById('range').value;
    fetch(`/apel?numar=${numar}`, {
        method: "GET"
    }).then((res) => {
        if(res.ok){
            console.log(res);
            return res;
        }
    }).then((data) => {
        console.log(data);
    })
    
})