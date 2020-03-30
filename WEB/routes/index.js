var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
var User = mongoose.model('Users');
var request = require('request');
router.get('/', function(req, res, next) {
  res.render("index");
});
router.get("/explore", (req,res)=>{
  if(req.query.yo_man == null){ var query = "all-time"}
  else{
    var query = req.query.yo_man;
    console.log(query);
  }
    
    var url = "http://localhost:5000/" + query;
    request(url, (error, response, body)=>{
    var name = JSON.parse(body);
    var result = name['Restaurant'];
    console.log(name);
    // res.render("explore");
    res.render("explore", {name : result});
  });
});

router.get("/whats", (req,res)=>{
  res.render("whats");
});

router.get("/aboutus", (req,res)=>{
  res.render("aboutus");
});

router.get("/regis", (req,res)=>{
  res.render("regis");
});

router.post("/regis", (req,res,next)=>{
  var doc = {
    name : req.body.name,
    year : req.body.year,
    veg : req.body.veg,
    fav : req.body.fav
  };
var users = new User(doc);
users.save((error)=>{
    console.log(users);
    if(error){ throw error; }
    res.json({message : "Data saved successfully.", status : "success"});
  });
});
module.exports = router;
