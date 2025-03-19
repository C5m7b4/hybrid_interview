from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class NumbersRequest(BaseModel):
    numbers: List[str]

class Peeps(BaseModel):
    id :int
    first_name: str
    last_name: str
    employeed: int
    hire_date: str
    gender: str

@app.post("/sum-even")
def sum_even_numbers(request: NumbersRequest):
    even_sum = sum(num for num in request.numbers if num % 2 == 1)
    # if you pass in 1,2,3,4,5,6,7,8,9, you should get 20
    return {"sum_even": even_sum}

@app.get('/peeps')
def get_peeps():
    # return all the peeps
    
    return JSONResponse(content={"error": 0, "success": True, "msg": "Not implemented yet", "peeps": []})





