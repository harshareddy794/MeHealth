//  Imporing express router
const express = require('express')
const router = express.Router();
const axios = require('axios');

// Imporing API function
const api = require('./api.js')



router.get("/home",(req,res)=>{
    res.render('depression-home')
})

router.post('/clasify', async(req,res)=>{
    const data = req.body
    var predection = await api.depression(data)
    if(predection.response==200){
        res.redirect("/depression/clasify?pred="+predection.predection)
    }else{
        res.send("Some thing went wrong")
    }
})

router.get("/clasify",(req,res)=>{
    var predection = parseInt(req.query.pred);
    res.render('depression-clasify',{data:predection});
})

router.get("/suggations",(req,res)=>{
    res.render('depression-suggations')
})


module.exports = router