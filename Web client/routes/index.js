//  Imporing express router
const express = require('express')
const router = express.Router();

// Imporing API function
const api = require('./api.js')

router.get("/",(req,res)=>{
    res.render('index')
})

router.get("/home",async(req,res)=>{
    var response = await api.covid_stats();
    res.render('home',{data:response});
})

router.get("/cov/stats",async(req,res)=>{
    var response = await api.covid_stats();
    res.send(response)
})
router.get("/mealone",(req,res)=>{
    res.render('chatbot')
})

router.get("/live-consultation",(req,res)=>{
    res.render('docters')
})

router.post("/mealone", async(req,res)=>{
    var command = req.body.message;
    if(command == 'Hi' || command == 'Hello'){
        res.send("Hello");
    }else if(command == 'facts' || command == 'jokes'){
        var api_res = await api.bot(command);
        if(api_res.response==200)
            res.send(Object.values(api_res)[0])
    }else{
        res.send('command not found')
    }
})

module.exports = router