//  Imporing express router
const express = require('express');
const { model, plugin } = require('mongoose');
const router = express.Router();
const donar  = require('../models/plasma.js')

// Imporing API function
const api = require('./api.js')

router.get("/home",(req,res)=>{
    res.render('covid-detection-home')
})


router.post('/clasify', async(req,res)=>{
    const data = req.body
    var predection = await api.covid(data)
    if(predection.response==200){
        res.redirect("/covid/clasify?pred="+predection.predection)
    }else{
        res.send("Some thing went wrong")
    }
})

router.get("/clasify",(req,res)=>{
    var predection = parseInt(req.query.pred);
    res.render('covid-clasify',{data:predection});
})


router.get('/precautions',(req,res)=>{
    res.render('precautions')
})

router.get('/after-precautions',(req,res)=>{
    res.render('aprecautions')
})

router.get("/plasma-donars",async(req,res)=>{
    const donarData = await donar.find({});
    res.render('pd-donar',{data:donarData})
})

router.get("/plasma-register",(req,res)=>{
    res.render('pd-register')
})

router.post("/plasma-register",async(req,res)=>{
    const donarData = new donar({...req.body})
    const data = await donarData.save();
    if(data){
        res.redirect('/covid/plasma-donars')
    }else{
        throw new Error('Something went wrong');
    }

})

module.exports = router;