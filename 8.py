from fastapi import FastAPI
app = FastAPI()

@app.get("/postcode/{code}")
def dig(code:str):
    l=len(code)
    if l !=10:
        return("تعداد رقم های کدپستی معتبر نیست")
    else:
        return("تعداد رقم های کد پستی معتبر است")