for(let i=0; i<10; ++i){
    let newElement = document.createElement('div');
    newElement.className = 'dreptunghi';

    newElement.addEventListener('click', (e) => {
        console.log(e);
        newElement.style.height = newElement.offsetHeight + 10  + 'px';
        event.stopPropagation();
    })

    document.body.append(newElement);
}

let varbody = document.getElementById('body');
varbody.style.height = "1000px";
varbody.addEventListener('click', (e) =>  {
    let divuri = document.getElementsByClassName('dreptunghi');
    for(let i=0; i<divuri.length; ++i){
        divuri[i].style.height = '50px';
    }
})
