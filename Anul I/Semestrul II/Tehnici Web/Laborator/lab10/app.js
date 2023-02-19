const express = require('express');
const app=express();

const hostname = '127.0.0.1';
const port = 3000;
const path=require("path");

const produse=["bmw series-5", "audi a6", "mercedes e-class", "bmw x5", "mercedes gle", "audi q7"];


// const server = http.createServer((req, res) => {
//   res.statusCode = 200;
//   res.setHeader('Content-Type', 'text/plain');
//   res.end('Hello World');
// });

// app.get("/", (req, res)=>{
//     res.send("Hello World");
// })

app.get("/about", (req, res)=>{
  res.send("Hello World");
})


// app.get("/", (req, res)=>{
//   res.sendFile(path.join(__dirname,"/views/index.html"));
// })

// app.get("/", (req, res)=>{
//   res.send(produse);
// })

// app.get("/products/:produsID", (req, res)=>{
//   const produsID=req.params.produsID;
//   res.send(produse[produsID]);
// })

app.get("/", (req, res)=>{
  res.send("Introdu ruta:/view_products,/new_products/, /delete_products/, /delete_all_products");
 
})

app.get("/view_products", (req, res)=>{
  res.send(produse);
 })

// Exercitiul 1

app.get("/new_products/:new_car", (req, res)=>{
  const new_product=req.params.new_car;
  produse.push(new_product);
  res.send(produse);
})


// Exerctiul 2

function verificare_index(id, produse){
  if(id>=produse.length){
    return false;
  }else{
    return true;
  }
}

let message='Invalid Id for product';

app.get("/delete_products/:produsID", (req, res)=>{
  const produsID=req.params.produsID;
  new_list_produse=[];
  if(verificare_index(produsID, produse)==false){
    res.send(message);
  }else{
    for(let i=0;i<produse.length;i++){
      if(i!=produsID){
        new_list_produse.push(produse[i]);
      }
    }
    res.send(new_list_produse)

  }
})


app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});



