from fastapi import FastAPI
app=FastAPI()

@app.get("/ship/{ship}")
def ch(ship:str):
    stat=["مجرد","متاهل"]
    if ship in stat:
        return("وضعیت تاهل درسته")
    else:
        return("وضعیت تاهل نادرستهُ")