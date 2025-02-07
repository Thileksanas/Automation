//import express

const express = require('express')
const cors = require ('cors');
const app= express()

//import dotenv
require('dotenv').config()

//import mongoose
const mongoose = require('mongoose')

app.use(express.json());
app.use(cors())

const router = require('./routes/user_route')

app.use('/user',router)

//db connection
mongoose.connect(process.env.DATABASE_URL)
.then(()=>console.log("mongodb connected"))
.catch(err =>console.log(err))




app.listen(process.env.PORT,()=>{
    console.log("server is running  ")
    
})

