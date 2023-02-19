const express = require('express');

const app = express();

app.use("/static", express.static("./static/"));

app.use(express.urlencoded({extended: false}));

let obiecte = [{nume:"agenda", greutate:"0.5"}, {nume:"telefon", greutate:"1"},
            {nume:"rucsac", greutate:"2.3"}, {nume:"caiet",greutate:"0.8"},
            {nume:"carte", greutate:"1"}, {nume:"tobe", greutate:"4"}];

app.get('/apel', (req, res) => {
    let numar = req.query.numar;
    let temp = [];
    for(let i=0; i<obiecte.length;++i){
        if (obiecte[i].greutate <= numar && obiecte[i].nume.includes('t')){
            temp.push(obiecte[i]);
        }
    }
    res.send(temp);
})
