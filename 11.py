from fastapi import FastAPI
app=FastAPI()

@app.get("/uni/{uni}")
def check(uni:str):
    list=[
        "فنی مهندسی","علوم پایه","علوم انسانی",
        "دامپزشکی","اقتصاد","کشاورزی","منابع طبیعی"
          ]
    if uni in list :
        return ("نام دانشکده درسته")
    else:
        return ("نام دانشکده نادرسته")