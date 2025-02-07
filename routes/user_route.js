const User_controller =require('../controllers/user_controller')

const express = require('express')

const router = express.Router()

//viewall
router.get('/view',User_controller.view_user_details)


//view by id
router.get('/view/:id',User_controller.view_user_details_by_id)

//create
router.post('/create',User_controller.create_user)

//update
router.put('/update/:id',User_controller.update_user)


//delete
router.delete('/delete/:id',User_controller.delete_user)

module.exports=router;