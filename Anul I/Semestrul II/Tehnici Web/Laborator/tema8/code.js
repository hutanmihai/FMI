//EXERCITIUL 3:
// for(let i=0;i<=9;i++){
//     let newDiv = document.createElement("div");
//     newDiv.style.display = "inline-block";
//     newDiv.style.border = "black 1px solid";
//     newDiv.style.width = "100px";
//     newDiv.style.height = "100px";
//     newDiv.style.marginLeft = "10px";
//     newDiv.style.backgroundColor = "lightblue";
//     newDiv.textContent = i;
//     document.body.append(newDiv);
// }

// document.addEventListener("keydown",(e) => {
//     document.getElementsByTagName("div")[e.key].style.backgroundColor = "yellow";
// })

// document.addEventListener("keyup",(e) => {
//     document.getElementsByTagName("div")[e.key].style.backgroundColor = "lightblue";
// })

//EXERCITIUL 4:
// let newDiv = document.createElement("div");
// newDiv.id = "patrat";
// newDiv.style.height= "200px";
// newDiv.style.width= "200px";
// newDiv.style.backgroundColor= "red";
// newDiv.style.position= "absolute";
// newDiv.style.left="600px";
// newDiv.style.top="200px";
// document.body.append(newDiv);
// document.addEventListener("keydown",(e) => {
//     console.log(e)
//     ev = e
//     let div = document.getElementById("patrat");
//     console.log(div.style.left)
//     console.log(div.style.top)
//     switch(ev.keyCode){
//         case 65:
//             div.style.left = (parseInt(div.style.left) - 10) + 'px';
//             break
//         case 68:
//             div.style.left = (parseInt(div.style.left) + 5) + 'px';
//             break
//         case 87:
//             div.style.top = (parseInt(div.style.top) - 10) + 'px';
//             break
//         case 83:
//             div.style.top = (parseInt(div.style.top) + 5) + 'px';
//             break
//     }   
// })

//EXERCITIUL 5:
// let nr = 1
// document.addEventListener("click",(e) => {
//     let newButton = document.createElement("button");
//     newButton.textContent = nr;
//     nr++;
//     console.log(e)
//     newButton.style.position = "absolute";
//     newButton.style.top = e.clientY + "px";
//     newButton.style.left = e.clientX + "px";
//     newButton.style.width = "70px";
//     newButton.style.height = "70px"
//     newButton.style.backgroundColor = changecolor();
//     document.body.append(newButton);
//     setTimeout(() => {
//         newButton.remove();
//     }, 5000);
// })

// function changecolor(){
//     return "rgb("+Math.random()*255+","+Math.random()*255+","+Math.random()*255+")";
// }