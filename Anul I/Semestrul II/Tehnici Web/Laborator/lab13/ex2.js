let range_input = document.createElement('input');
let div1 = document.createElement('div');

let range = window.localStorage.getItem('rangevalue');

range_input.id = "rangeinput";
range_input.type = 'range';
range_input.min = 4;
range_input.max = 10;
if (range != null){
range_input.value = range;
}
else range_input.value = 7;
div1.style.height = '90vh';
div1.style.width = '90vw';
div1.style.backgroundColor = 'grey';
div1.style.position = 'relative';
div1.id = "parinte";

document.body.append(range_input);
document.body.append(div1)

range_input.onchange = () => {
    let N = document.getElementById('rangeinput').value;
    localStorage.setItem('rangevalue', N);
    for(let i=0; i<N; ++i){
        let curent = document.createElement('div');
        curent.classList.add('copil');
        curent.style.position = 'absolute';
        curent.style.width = '50px';
        curent.style.height = '50px';
        curent.style.backgroundColor = 'red';
        curent.style.top = Math.floor(Math.random() * 500)+"px";
        curent.style.left = Math.floor(Math.random() * 800)+"px";
        div1.append(curent);
    }
}

let copii = document.querySelectorAll(".copil");

copii.forEach(element => {
    element.addEventListener("onclick", (e) => {
        e.classList.add('activ');
        console.log(e);
    })
});

let activi = document.querySelectorAll(".activ");

activi.forEach(element => {
    element.addEventListener("keydown", (e) => {
        if (e.keyCode == '37'){
            e.style.left = (parseInt(e.style.left) + 100) + 'px';
        }
        else if (e.keyCode == '39'){
            e.style.left = (parseInt(e.style.left) - 100) + 'px';
        }
})
})


