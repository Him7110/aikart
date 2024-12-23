const express = require('express')
const cookieParser = require('cookie-parser');
const authRouter = require('./routes/authRoutes.js');
const userRouter=require("./routes/userRoutes.js");

const aiRoutes = require('./routes/aiRoutes.js');
const dbConnect=require('./utils/databaseConnect.js');
//const {upload} = require('./utils/cloudinary.js')
const upload = require('./utils/fileupload.js')


const cors = require('cors');
require('dotenv').config();

dbConnect();



const app = express();
app.use(express.json())
app.use(cookieParser());
app.use(cors({
  origin: ['https://aikart.vercel.app/'],
  credentials: true
}));
app.use(express.static("aikart/backend/public"));

app.use('/api/auth', authRouter);
app.use('/api/user', userRouter);

app.use('/ai', aiRoutes);

app.post('/upload', upload.single("file"), (req, res) =>{
  if(!req.file)return;
  var destin = req.file.destination;
  destin = "../backend" + destin.substring(1) + req.file.filename;
  req.file["destin"] = destin;
  console.log(destin);
  res.json(req.file)
});

app.listen(process.env.PORT, () => {
  console.log(`server is running on port ${process.env.PORT}`);
})

