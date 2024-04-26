from fastapi import FastAPI
import re
app=FastAPI()

@app.get("/word/{word}")
def valid(word:str):
    l=len(word)
    if word.isalpha() == False :
        return("ورودی نباید شامل کارکتر های خاص باشد")
    for i in range(0,l):
        if  "a"<=word[i]<="z" or  "A"<=word[i]<="Z":
            return("ورودی باید شامل کارکتر های فارسی باشد")
    if l>10:
        return("ورودی باید کمتر از 10 کارکتر باشد")

    else:
        return("ورودی درست است")