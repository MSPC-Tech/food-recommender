var express = require("express");

var app = express();

app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');
app.use(express.static(__dirname + '/public'));
app.get("/", function(req,res){
    res.render("index.html")
});

app.get("/aboutus", (req,res)=>{
    res.render("aboutus.html");
});

app.get("*", (req,res)=>{
    res.send("PAGE NOT FOUND 404");
});

app.listen(8080, ()=>{
    console.log("SERVER HAS STARTED");
});