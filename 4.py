from fastapi import FastAPI
app=FastAPI()

@app.get("/seris/{num}")
def passy(num):
    l=len(num)
    harf=num[0]
    ragham=num[1:9]

    if l!=9 or harf==int or ragham !=int:
        return ("قالب سریال شناسنامه معتبر نیست")
    else:
        ("قالب سریال شناسنامه معتبر است")