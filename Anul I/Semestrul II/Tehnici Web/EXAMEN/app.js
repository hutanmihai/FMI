const express = require('express');
const app = express();
const path = require('path');
const router = express.Router();
app.use(express.json())
app.use(express.urlencoded({extended: false}));
app.use('/', router);

router.get('/', function (req, res) {
    res.sendFile(path.join(__dirname + '/p4.html'));
});

app.post('/post', function (req, res) {
    let optiune = req.body.selector;
    let sir = req.body.inputnr;
    let array = sir.split(' ');
    let newarray = [];
    for (let element of array) {
        let numar = Number(element);
        if (Number.isInteger(numar) === true) {
            if (optiune === 'par') {
                if (numar % 2 === 0) {
                    newarray.push(numar);
                }
            } else if (optiune === 'impar') {
                if (numar % 2 === 1) {
                    newarray.push(numar);
                }
            }
        } else {
            res.send('imposibil');
        }
    }
    for (let element of newarray) {
        if (element === 0) {
            res.send('imposibil');
            //Tratam cazul in care se baga mai mult de un spatiu si cazul in care avem 0 impartit la ceva.
        }
    }
    let string = newarray.join(',');
    res.send(string);
})

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Our express server is up on port ${port}`);
});