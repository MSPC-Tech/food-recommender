var express = require("express");
var bodyparser = require("body-parser");
var request = require("request");
var zomato = require("zomato-api");
var client = zomato({
    userKey: 'ecc34bdd86f2979895de04d1fe80922c'
})
var app = express();

app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');
app.use(express.static(__dirname + '/public'));
app.get("/", function(req,res){
    res.render("index.html");
});

// ZOMATO API

app.get("/result", (req,res)=>{

    client.getCities({q: 'ahmedabad'})
        .then(res=> console.log(res))
    // var query = req.query.;
    // url = "https://developers.zomato.com/api/v2.1/cities/?q=" + query + "&apikey=ecc34bdd86f2979895de04d1fe80922c";
    // request(url, (error, response, body)=> {
    // request(post, function(error, response, body) {
    //     console.log('error', error);
    //     console.log('body', body);
    //     console.log('response', response);
        // if(!error && response.statusCode == 200){
        //     console.log(JSON.parse(body));
        //     res.render("result.html", {});
        // }
    // });
});

app.get("/explore", (req,res)=>{
    res.render("explore.html");
});

app.get("/whats", (req,res)=>{
    res.render("whats.html");
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