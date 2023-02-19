// afisare in consola + alerta + model initializare (!!! VAR ESTE PRIMITIV) !!! VAR E GLOBAL, LET E LOCAL, CONST (Imutabil)
console.log("Mesaj")
alert("Pop up!")
let a,b,c,d;
a = 7; b = 7; c = a + b; d = "Mesaj";
//  let array = [5, 7, "Mesaj", [ ... (alt array) ], false];
let array = [1,2,3,4,5,6,7,"opt","noua","zece"]

// for si afisare

for (let i=0;i<array.length;++i){
    console.log(array[i])
}

// alt tip de for by element nu by position

array.forEach(element => {
    console.log(element);
})

// model de json

let object = {
    "nume": "Hutan",
    "prenume": "Mihai",
    "email": "hutanmihai29@gmail.com",
    note: {"tehnici web": 10,
            "Poo": 4
        }
}

// apelare + afisare obiecte

console.log(object.nume)
console.log(object.note.Poo)
console.log(object.note["tehnici web"])

function functionName(){
    document.getElementById("text_random").innerHTML="Alt text!";
};

let nume = "Hutan Mihai-Alexandru";
function myName(){
    document.getElementById("numele_meu").innerHTML=nume;
}

array2 = ["5", "5", 5, 3, 2, "A", "B", 3]
let Unique = array2.filter((element, index) => {
    return array2.indexOf(element) === index;
})
console.log(Unique)
