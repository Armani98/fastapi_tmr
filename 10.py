from fastapi import FastAPI
app=FastAPI()

@app.get("/phone/{phone}")
def check(phone:str):
    l=len(phone)
    numbers_list = ["041", "044", "045", "031",
                "026", "084", "077", "021",
                "038", "056", "051", "058",
                "061", "024", "023", "054",
                "071", "028", "025", "087",
                "034", "083", "074", "017",
                "013", "066", "011", "086",
                "076", "081", "035"]

    if phone[0:3] in numbers_list and l==11 :
        return("شماره درست است")
    else:
        return("شماره نادرست است")