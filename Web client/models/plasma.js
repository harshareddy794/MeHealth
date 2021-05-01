const mongoose = require('mongoose')
const { Schema } = mongoose;

const donarSchema = new Schema({
    name :  String, 
    state:   String,
    blood : String,
    number : Number,  
    date: String,
});

const donar = mongoose.model('donar', donarSchema);

module.exports = donar;