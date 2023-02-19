function myName(nume){
    document.getElementById("numele_meu").innerHTML=nume;
}

let vector = [5, 5, '5', 3, 2, 'A', 'B', 'A', 3];

let rez1=vector.filter(f);

function f(x){
    let nr=0;
    for(let i=0;i<vector.length;i++){
        if(vector[i]===x){
            nr+=1;
        }
    }
    if(nr==1){
        return 1;
    }else{
        return 0;
    }
}
console.log(rez1);

let rez2 = [];

for(let i=0;i<vector.length;i++){
    let nr = 0
    for (let j=0;j<vector.length;j++){
        if(vector[i] === vector[j]){
            nr += 1;
        }
    }
    if (nr == 1){
        rez2.push(vector[i]);
    }
}

console.log(rez2);
