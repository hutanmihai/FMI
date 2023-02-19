fetch("https://exemplu-api-fmi.herokuapp.com/bomb")
  .then((response) => {
    if (response.status >= 400) {
      throw new Error("bad");
    }
    response.json().then((data) => console.log(data));
  })
  .catch((err) => console.log(`error: ${err}`));
