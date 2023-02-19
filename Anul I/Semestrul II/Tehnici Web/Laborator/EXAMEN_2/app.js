const express = require('express');
const app = express();
const path = require('path');
const router = express.Router();
app.use(express.json())
app.use(express.urlencoded({extended: false}));
app.use('/', router);

obiecte = [{nume: "agenda", greutate: "0.5"}, {nume: "telefon", greutate: "1"},
    {nume: "rucsac", greutate: "2.3"}, {
        nume: "caiet",
        greutate: "0.8"
    }, {nume: "carte", greutate: "1"}, {nume: "tobe", greutate: "4"}]

router.get('/', function (req, res) {
    res.sendFile(path.join(__dirname + '/p4.html'));
});

app.get('/get', function (req, res){
    let numar = req.query.numar;
    let array = [];
    for (let obiect of obiecte){
        if (obiect.nume.includes('t') === true && obiect.greutate <= numar)
            array.push(obiect);
    }
    res.send(array);
})

app.post('/', function (req, res){

})

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Our express server is up on port ${port}`);
});