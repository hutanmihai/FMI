const BASE_URL = "https://exemplu-api-fmi.herokuapp.com"

const getBombData = () => {
    fetch(`${BASE_URL}/bomb`)
        .then((chestie) => {
            console.log("raspunsul este " + chestie)

            if (chestie.status >= 400){
                throw new Error ("N-a functionat!")
            }

            chestie.json().then((jsonResponse) => {
                console.log("Raspunsul din Fetch API", jsonResponse);
                return jsonResponse;
            })
        })
        .catch((eroare) => {
            console.log("Eroarea este: " + eroare);
        })
}

getBombData();