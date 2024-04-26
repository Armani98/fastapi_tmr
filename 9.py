from fastapi import FastAPI
app=FastAPI()

@app.get("/cphone/{num}")
def stan(num:str):
    l=len(num)
    if num[0]=="0" and num[1]=="9" and l==11:
        return("شماره موبایل معتبر است")
    else:
        return("شماره ی موبایل معتبر نیست")