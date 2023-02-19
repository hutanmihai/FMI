const express = require("express");
const path = require("path");
const app = express();

const port = 3000;

let products = ["product1", "product2", "product3"];

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "/views/index.html"));
});

app.get("/products", (req, res) => {
  res.send(products);
});

app.get("/products/:productId", (req, res) => {
  const productId = req.params.productId;
  res.send(products[productId]);
});

app.post("/products/add/:productName", (req, res) => {
  const productName = req.params.productName;
  products = [...products, productName];
  res.send(products);
});

app.delete("/products/delete/:productId", (req, res) => {
  const productId = parseInt(req.params.productId);
  if (productId > products.length - 1) {
    res.send({ error: `Invalid id ${productId}.` });
  } else {
    products = products.filter((product, id) => id !== productId);
    res.send(products);
  }
});

app.delete("/products/delete_all", (req, res) => {
  products = [];
  res.send({ msg: "Products deleted successfully." });
});

app.listen(port, () =>
  console.log(`Server running at http://localhost:${port}/`)
);
