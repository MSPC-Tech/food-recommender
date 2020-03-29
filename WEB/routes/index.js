var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
var User = mongoose.model('Users')
router.get('/', function(req, res, next) {
  res.render("index");
});
router.get("/explore", (req,res)=>{
  res.render("explore");
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
    year : req.body.year
  };
var users = new user(doc);
users.save((error)=>{
    console.log(users);
    if(error){ throw error; }
    res.json({message : "Data saved successfully.", status : "success"});
  });
});
module.exports = router;
