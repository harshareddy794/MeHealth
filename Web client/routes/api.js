const axios = require('axios');

const bot = async(command)=>{
    if(command == "facts"){
        var response = await axios.get("https://me-health.herokuapp.com/api/facts")
        response = response.data
        return response
    }else if(command == "jokes"){
        var response = await axios.get("https://me-health.herokuapp.com/api/jokes")
        // var response = await axios.get("https://me-health.herokuapp.com/api/jokes")
        response = response.data
        return response
    }
}

const depression = async(data) =>{
    // var response = await axios.post("https://me-health.herokuapp.com/api/depression-detection",data)
    var response = await axios.post("http://127.0.0.1:5000/api/depression-detection",data)
    response = response.data
    return response;
}


const covid = async(data) =>{
    // var response = await axios.post("https://me-health.herokuapp.com/api/covid-detection",data)
    var response = await axios.post("http://127.0.0.1:5000/api/covid-detection",data)
    response = response.data
    return response;
}

const covid_stats = async()=>{
    var response = await axios('https://api.covid19india.org/data.json')
    response = response.data;
    response = response.cases_time_series;
    for(i=0;i<response.length;i++){
        delete response[i].date;
        response[i].dateymd = (response[i].dateymd).split('-')
    }
    return response;
    
}

module.exports = {
    bot,
    depression,
    covid,
    covid_stats,
}