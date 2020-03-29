var mongoose = require("mongoose");

var userSchema = new mongoose.Schema({
        name: {type: String, required: [ true, 'Name is mandatory'], unique: true}, 
        year: {type: String, required: [true, 'Please specify your year']},
        // : {type: String, required: true},
        // veg: {type: String, required: true},
    });
module.exports = mongoose.model('Users', userSchema);
