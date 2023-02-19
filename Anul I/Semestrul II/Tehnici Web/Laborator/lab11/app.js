const express = require("express");

const app = express();
const PORT = 3000;

const fructe = ["mere", "pere", "banane"];

app.set("view engine", "ejs");
app.use("/static", express.static("./static/"));

app.get("/products", (req, res) => {
  res.json(fructe);
});

app.get("/", (req, res) => {
  res.render("./html/index");
});

app.listen(PORT, () => "a");
