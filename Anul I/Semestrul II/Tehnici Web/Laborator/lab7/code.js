function functionInput(){
    let input = document.getElementById("UserInput").value;
    document.getElementById("paragraph").innerHTML=input;
}

// // innerText SAU textContent in loc de innerHTML;

// const div=document.createElement("div");
// div.innerHTML = "<strong>Text + HTML in JS</strong>";
// document.body.append(div)

// // RANDUL 2 E GRESIT // AR TREBUI SA FIE ASA:
// const strong = document.createElement("strong");
// strong.innerText = "Text + HTML in JS";
// div.append(strong);
// document.body.append(div);


//Math.random() returneaza [0,1]
//pt a returna alte intervale folosim Math.random()*(max-min)+min  (min fiind capatul din stanga si max capatul din dreapta al intervalului dorit)

const element = document.getElementById("div")
function changecolor(){
    element.style.backgroundColor = "rgb("+Math.random()*255+","+Math.random()*255+","+Math.random()*255+")";
}
