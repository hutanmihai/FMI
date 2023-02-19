const express = require('express');
const app = express();
app.use(express.json());
app.use('/post', express.urlencoded({extended: true}));

persoane = [{nume: "Ion", sex: "m", varsta: 3}, {nume: "Oana", sex: "f", varsta: 23}, {
    nume: "Daria",
    sex: "f",
    varsta: 10
}, {nume: "Mihai", sex: "m", varsta: 19}, {nume: "Gabriel", sex: "m", varsta: 22}, {
    nume: "Simona",
    sex: "f",
    varsta: 11
}, {nume: "Bogdan", sex: "m", varsta: 28}];

app.get("/", function (req, res) {
    res.sendFile(__dirname + "/p4.html");
});

app.post('/', function (req, res) {
    const nume = req.body.nume;
    console.log(nume);
    let gasit = false;
    let baiat = false;
    let maj = false;
    for (let persoana of persoane) {
        if (nume === persoana.nume) {
            gasit = true;
            if (persoana.varsta >= 18) {
                maj = true;
            }
            if (persoana.sex === 'm') {
                baiat = true;
            }
        }
    }
    let string;
    if (gasit === true) {
        if (baiat === true) {
            string = 'baiat';
        } else string = 'fata';
        if (maj === true) {
            string += ", este major";
        } else string += ", este minor";
        res.send(string);
    }
    if (gasit === false) {
        res.send('Nu exista numele cautat!');
    }
})

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Our express server is up on port ${port}`);
});