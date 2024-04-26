from fastapi import FastAPI
app=FastAPI()

@app.get("/meli/{meli}")
def check(meli):

    l = len(meli)
    sum = 0
    for i in range(0, l - 1):
        c = ord(meli[i])
        c -= 48
        sum = sum + c * (l - i)
    r = sum % 11
    c = ord(meli[l - 1])
    c -= 48
    if r > 2:
        r = 11 - r
    if r == c:
        return("کد ملی معتبر است")
    else:
        return("کد ملی معتبر نیست")