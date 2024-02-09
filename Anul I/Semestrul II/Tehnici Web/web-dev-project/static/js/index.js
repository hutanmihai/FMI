let filme = [
    {
        "nume": "DON'T LOOK UP",
        "gen": "comedie",
        "anAparitie": "2021",
        "actori": ["Leonardo DiCaprio", "Jennifer Lawrence", "Timothee Chalamet"],
        "premiat": true
    },
    {
        "nume": "TIK TIK BOOM",
        "gen": "drama/biografie",
        "anAparitie": "2021",
        "actori": ["Andrew Garfield", "Vanessa Hudgens", "Alexandra Shipp"],
        "premiat": false
    },
    {
        "nume": "DUNE",
        "gen": "SF",
        "anAparitie": "2021",
        "actori": ["Timothee Chalamet", "Zendaya", "Jason Momoa"],
        "premiat": true
    },
    {
        "nume": "JOKER",
        "gen": "drama/thriller",
        "anAparitie": "2019",
        "actori": ["Joaquin Phoenix", "Robert De Niro", "Zazie Beetz"],
        "premiat": true
    },
    {
        "nume": "AD ASTRA",
        "gen": "SF",
        "anAparitie": "2019",
        "actori": ["Brad Pitt", "Tommy Lee Jones", "Ruth Negga"],
        "premiat": false
    },
    {
        "nume": "1917",
        "gen": "razboi",
        "anAparitie": "2019",
        "actori": ["George MacKay", "Richard Madden", "Benedict Cumberbatch"],
        "premiat": true
    }
]

let com1 = document.getElementById("ComunityTextOne");
let com2 = document.getElementById("ComunityTextTwo")

let filmePremiate = filme.filter(function (el) {
    return el.premiat == true;
})

filmePremiate.forEach(elem => {
    if (elem.anAparitie == "2019") {
        com1.innerHTML += "<br>" + "<span class='2019'>" + elem.nume + "</span>" + "<br>Genul filmului: " + elem.gen + "<br>Actorii cei mai cunoscuti sunt:<br>" + elem.actori.join(", ") + "<br>";
    } else com2.innerHTML += "<br>" + "<span class='2021'>" + elem.nume + "</span>" + "<br>Genul filmului: " + elem.gen + "<br>Actorii cei mai cunoscuti sunt:<br>" + elem.actori.join(", ") + "<br>";
})

let filme2019 = document.getElementsByClassName('2019');
let filme2021 = document.getElementsByClassName('2021');

for (let i = 0; i < filme2019.length; ++i) {
    filme2019[i].style.cursor = 'pointer';
    filme2019[i].addEventListener('click', (e) => {
        alert('Acest film a aparut in anul 2019!');
        event.stopPropagation();
    })
}

for (let i = 0; i < filme2021.length; ++i) {
    filme2021[i].style.cursor = 'pointer';
    filme2021[i].addEventListener('click', (e) => {
        alert('Acest film a aparut in anul 2021!');
        event.stopPropagation();
    })
}

document.getElementById('ComunityBox').style.cursor = 'pointer';

document.getElementById('ComunityBox').addEventListener('click', (e) => {
    alert('The 95th Oscars will be held on Sunday, March 12, 2023, the Academy of Motion Picture Arts and Sciences and ABC announced on Friday. As always, the ceremony will take place at the Dolby Theatre at Ovation Hollywood and will air live on ABC in more than 200 territories around the world.');
})