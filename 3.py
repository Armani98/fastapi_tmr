from fastapi import FastAPI
app=FastAPI()
@app.get("/date/{year}/{month}/{day}")
def birth(year:int,month:int,day:int):
    if 1300<year<1403 and 0<month<13 and 0<day<31:
        return("تاریخ تولد درست است")
    else: 
        return ("تاریخ تولد نادرست است")