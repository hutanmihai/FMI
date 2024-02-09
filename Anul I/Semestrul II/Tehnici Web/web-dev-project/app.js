const express = require('express');
const app = express();
const fs = require('fs');

let users = [];

app.use(express.json());

app.set('view engine', 'ejs');

app.use("/static", express.static("./static/"));

app.use(express.urlencoded({extended: false}));

app.get('/', (req, res) => {
    res.render('register');
});

app.get('/login', (req, res) => {
    res.render('login');
});

app.get('/index', (req, res) => {
    res.render('index');
});

app.get('/myaccount', (req, res) => {
    res.render('myaccount');
});

app.get('/reviews', (req, res) => {
    res.render('reviews');
});

// app.post("/register-post", (req, res) => {
//     users.push({
//         email: req.body.email,
//         password: req.body.pass
//     })
//     res.redirect('/login')
// })
//
// app.get("/login-get", (req, res) => {
//     const email = req.query.email;
//     const pass = req.query.password;
//     let gasit = 0;
//     users.forEach(element => {
//         if (element.email == email && element.password == pass) {
//             gasit = 1;
//             res.send('');
//         }
//     })
//     if (gasit == 0) {
//         res.status(400).send('');
//     }
// })
//
// app.put("/change-password", (req, res) => {
//     const email = req.query.email;
//     const pass = req.query.password;
//     let pos;
//     for (let i = 0; i < users.length; ++i) {
//         if (users[i].email == email && users[i].password == pass) {
//             pos = i;
//         }
//     }
//     users[pos].password = makePass(8);
//     let password = users[pos].password;
//     res.send({password});
// })
//
// app.delete("/delete-account", (req, res) => {
//     const email = req.query.email;
//     const pass = req.query.password;
//     let pos;
//     for (let i = 0; i < users.length; ++i) {
//         if (users[i].email == email && users[i].password == pass) {
//             pos = i;
//         }
//     }
//     users = users.splice(pos, 1);
//     res.send('');
// })

// ------------------------------------------------------------------- //

app.post("/register-post", (req, res) => {
    let newuser = {
        email: req.body.email,
        password: req.body.pass
    };
    let rawfile = fs.readFileSync('users.json');
    let file = JSON.parse(rawfile);
    file.push(newuser);
    fs.writeFileSync('users.json', JSON.stringify(file));
    res.redirect('/login')
})

app.get("/login-get", (req, res) => {
    const email = req.query.email;
    const pass = req.query.password;
    let rawfile = fs.readFileSync('users.json');
    let file = JSON.parse(rawfile);
    let gasit = false;
    for (let i = 0; i < file.length; ++i)
        if (file[i].password == pass && file[i].email == email) {
            gasit = true;
            res.send('')
        }

    fs.writeFileSync('users.json', JSON.stringify(file));
    if (gasit === false) {
        res.status(400).send('');
    }

})

app.put("/change-password", (req, res) => {
    const email = req.query.email;
    const pass = req.query.password;
    let rawfile = fs.readFileSync('users.json');
    let file = JSON.parse(rawfile);
    let pos = 0;
    for (let i = 0; i < file.length; ++i) {
        if (file[i].password == pass && file[i].email == email) {
            pos = i;
        }
    }
    file[pos].password = makePass(10);
    fs.writeFileSync('users.json', JSON.stringify(file));
    let parolanoua = file[pos].password;
    res.send({parolanoua});
})

app.delete("/delete-account", (req, res) => {
    const email = req.query.email;
    const pass = req.query.password;
    let rawfile = fs.readFileSync('users.json');
    let file = JSON.parse(rawfile);
    let pos;
    for (let i = 0; i < file.length; ++i) {
        if (file[i].password == pass && file[i].email == email) {
            pos = i;
            break
        }
    }
    file.splice(pos, 1);
    fs.writeFileSync('users.json', JSON.stringify(file));
    res.send('');
})

// --------------------------------------------------------------------//

app.get("*", (req, res) => {
    res.render("error_page");
})

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Our express server is up on port ${port}`);
});

function makePass(length) {
    let result = '';
    let characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let charactersLength = characters.length;
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() *
            charactersLength));
    }
    return result;
}