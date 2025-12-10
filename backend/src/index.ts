import express from "express";
import cors from "cors";
import {router as healthRouter} from "./routes/health";
import dotenv from "dotenv";

dotenv.config();
const app = express();
app.use(cors());
app.use(express.json());

app.use("/health", healthRouter);

app.listen(process.env.PORT, () => console.log(`Server running on port ${process.env.PORT}`));