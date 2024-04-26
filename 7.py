from fastapi import FastAPI
app=FastAPI()
@app.get("/address/{address}")
def add(address:str):
    l=len(address)
    if l<=100:
        return("آدرس درست است")
    else:
        return("آدرس درست نیست")