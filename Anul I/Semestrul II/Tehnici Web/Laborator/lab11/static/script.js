const re = new RegExp("ab*c");

const ul = document.getElementsByTagName("ul")[0];

document.getElementById("afis").addEventListener("click", () => {
  fetch("http://localhost:3000/products")
    .then((response) => response.json())
    .then((data) =>
      data.forEach((el) => {
        const element = document.createElement("li");
        element.textContent = el;
        ul.append(element);
      })
    );
});
