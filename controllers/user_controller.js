const User = require('../models/user_model')

const view_user_details = async(req,res)=>{
    try{
    const user_view= await User.find()
    res.status(200).json(user_view)
}
catch(error){
    res.status(500).json({message:error.message})
}

}



//view by id

const view_user_details_by_id =async(req,res)=>{
    try{
        const id = req.params.id;
        const user_id = await User.findById(id);
        res.status(200).json(user_id )
    }

    catch(error){
        res.status(500).json({message:error.message})
    }

}

//create

const create_user= async(req,res)=>{
    try{
        const user = await User.create(req.body);
        res.status(200).json(user)
    }

    catch(error){
        res.status(500).json({message:error.message})
    }
}



//update

const update_user= async(req,res)=>{
    try{
        const id = req.params.id;
        const updated_user = await User.findByIdAndUpdate(id,req.body)
        res.status(200).json(updated_user)
    }
    catch(error){
        res.status(500).json({message:error.message})
    }

}

//delete

const delete_user= async(req,res)=>{
    try{
        const id = req.params.id;
        const deleted_user = await User.findByIdAndDelete(id)
        res.status(200).json({message:"user details deleted successfully"})
    }

    catch(error){
        res.status(500).json({message:error.message})
    }

}





module.exports={view_user_details,view_user_details_by_id,create_user,update_user,delete_user };

