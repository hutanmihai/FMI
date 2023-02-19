// let element1 = document.getElementById("div1");
// element1.addEventListener("click",func1);
// function func1(e){
//     console.log(e);
// }

// document.addEventListener("keydown",func2);
// function func2(e){
//     console.log(e);
// }

// function addElement(){
//     const newDiv = document.createElement("div")
//     newDiv.style.border = "black 1px solid";
//     newDiv.addEventListener("click", changecolour);
//     return newDiv;
// }
// function changecolour(e){
//     e.style.backgroundColor = "yellow";
// }

// for(let i=0; i<9; i++){
//     document.body.append.addElement();
// }

for(let i=0;i<=9;i++){
    let newDiv = document.createElement("div");
    newDiv.style.display = "inline-block";
    newDiv.style.border = "black 1px solid";
    newDiv.style.width = "100px";
    newDiv.style.height = "100px";
    newDiv.style.marginLeft = "10px";
    newDiv.style.backgroundColor = "grey";
    newDiv.textContent = i;
    document.body.append(newDiv);
}

document.addEventListener("keydown",(e) => {
    document.getElementsByTagName("div")[e.key].style.backgroundColor = "yellow";
})

document.addEventListener("keyup",(e) => {
    document.getElementsByTagName("div")[e.key].style.backgroundColor = "grey";
})

document.addEventListener("click",(e) => {
    let newButton = document.createElement("button");
    newButton.textContent = "Button";
    newButton.style.position = "absolute";
    newButton.style.top = e.clientY + "px";
    newButton.style.left = e.clientX + "px";
    newButton.style.width = "100px";
    newButton.style.height = "100px"
    newButton.style.backgroundColor = changecolor();
    document.body.append(newButton);
    setTimeout(() => {
        newButton.remove();
    }, 5000);
})

function changecolor(){
    return "rgb("+Math.random()*255+","+Math.random()*255+","+Math.random()*255+")";
}




