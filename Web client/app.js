const express = require('express')
const app = express();
const bodyParser = require('body-parser')
const cors = require("cors");
const mongoose = require('mongoose');

// Middleware use
app.use(express.static("public"))
app.set("view engine","ejs")
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cors());


// DB connect 
mongoose.connect('mongodb://localhost:27017/mehealth', {useNewUrlParser: true, useUnifiedTopology: true});

// Routes in use
const routes = require('./routes/index.js')
const depressionRoutes = require('./routes/depression.js')
const covidRoutes = require('./routes/covid.js')

// Routes
app.use('/covid',covidRoutes);
app.use('/depression',depressionRoutes);
app.use('/',routes);

app.listen(3002,()=>{
    console.log("server running at port",3002);
})