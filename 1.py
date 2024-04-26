from fastapi import FastAPI
app=FastAPI()

@app.get("/number/{num}")
def check(num:str):
    l=len(num)
    list = [str(i).zfill(2) for i in range(1, 100)]
    year=["400","401","402"]
    if l!=11:
        return("شماره ی دانشجویی باید 11 رقم باشد.تعداد ارقام دانشجویی وارد شده نادرست است")
    if num[0:3] not in year:
        return ("قسمت سال نادرست است")
    if num[3:9] !="114150":
        return("قسمت ثابت نادرست است")
    if num[9:11] not in list:
        return("قسمت اندیس نادرست است")
    else:
        return("شماره دانشجویی درست است",num)