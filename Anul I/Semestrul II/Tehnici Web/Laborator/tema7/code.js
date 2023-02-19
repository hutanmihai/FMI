// Exercitiul 1
function SubmitFunction(){
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    console.log(name, email, password);
}

// Exercitiul 2
function increase(){
 let plus = document.getElementsByClassName("change");
 for(let i=0;i<plus.length;i++){
     let element = plus[i];
     element.style.fontSize = "1.5rem";
 }   
}
function decrease(){
 let minus = document.getElementsByClassName("change");
 for(let i=0;i<minus.length;i++){
     let element = minus[i];
     element.style.fontSize = "0.8rem";
 }   

}
// Exercitiul 3
function up(){
    let div = document.getElementById("patrat");
    div.style.top = parseInt(div.style.top) - 5 + 'px';
}
function left(){
    let div = document.getElementById("patrat");
    div.style.left = parseInt(div.style.left) - 5 + 'px';
}
function down(){
    let div = document.getElementById("patrat");
    div.style.top = parseInt(div.style.top) + 5 + 'px';
}
function right(){
    let div = document.getElementById("patrat");
    div.style.left = parseInt(div.style.left) + 5 + 'px';
}
// Exercitiul 4
// @TODO
function showrandomstrings(){  
    let array = ["Am plecat la mare","Am plecat la munte","Mergem la film","Nu am fost niciodata cu avionul","Imi plac serialele","Imi plac filmele"];
    document.getElementById("empty").innerHTML = array[Math.floor(Math.random()*6)];
}